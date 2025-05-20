from rich.markdown import Markdown
from rich.console import Console
from rich.live import Live
from dotenv import load_dotenv
import asyncio
import pathlib
import sys
import os

from pydantic_ai import Agent
from openai import AsyncOpenAI, OpenAI
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


import mcp_client

# Get the directory where the current script is located
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
# Define the path to the config file relative to the script directory
CONFIG_FILE = SCRIPT_DIR / "mcp_config.json"

# Constants
MAX_HISTORY_LENGTH = 50  # Maximum number of messages to keep in history

load_dotenv()

# Initialize Rich console for pretty output
console = Console()

def get_model():
    ollama = OpenAIModel(model_name='qwen2.5', provider=OpenAIProvider(base_url='http://localhost:11434/v1'))
    return ollama

async def get_pydantic_ai_agent():
    client = mcp_client.MCPClient()
    client.load_servers(str(CONFIG_FILE))
    tools = await client.start()
    system_prompt = (
    "You are a local intelligent agent with access to a suite of MCP-compatible tools. "
    "Your role is to assist the user by coordinating these tools effectively to complete complex tasks. "
    "You can call tools, combine outputs, manage workflows, and adapt your behavior based on context. "
    "Always reason through the user's intent, decide which tools to invoke, and return clear, helpful responses or actions. "
    "Be efficient, concise, and straightforward by answering the question or request directly. Avoid outputting a bunch of irrelevant texts."
    "When in doubt, ask the user for clarification."
    )
    return client, Agent(model=get_model(), tools=tools, system_prompt=system_prompt)

def trim_message_history(messages):
    """Trim message history to prevent memory issues in long conversations."""
    if len(messages) <= MAX_HISTORY_LENGTH:
        return messages
    
    # Keep the most recent messages
    return messages[-MAX_HISTORY_LENGTH:]



async def main():
    console.print("[bold blue]=== Pydantic AI MCP CLI Chat ===")
    console.print("Type '[bold green]exit[/bold green]' to quit the chat")
    console.print("Type '[bold yellow]reset[/bold yellow]' to reset the conversation")
    
    # Initialize the agent and message history
    mcp_client, mcp_agent = await get_pydantic_ai_agent()
    messages = []
    
    try:
        while True:
            # Get user input
            user_input = input("\n[You] ")
            
            # Check if user wants to exit
            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                console.print("[bold blue]Goodbye!")
                break
                
            # Check if user wants to reset conversation
            if user_input.lower() == 'reset':
                messages = []
                console.print("[bold yellow]Conversation reset!")
                continue
            
            try:
                # Process the user input and output the response
                console.print("\n[Assistant]")
                

                result = await mcp_agent.run(user_input, message_history=messages)
              
                
                # Extract the text from the result
                result_text = result.data
                # Render the result as Markdown
                markdown = Markdown(result_text)
                console.print(markdown)
                
                # Add the new messages to the chat history and trim if needed
                messages.extend(result.all_messages())
                messages = trim_message_history(messages)
                
            except KeyboardInterrupt:
                console.print("\n[bold red]Operation interrupted by user.")
                continue
            except Exception as e:
                console.print(f"\n[bold red][Error] {str(e)}")
                console.print("You can continue with your next question or type 'reset' to start a new conversation.")
    
    except KeyboardInterrupt:
        console.print("\n[bold red]Program interrupted by user. Exiting...")
    finally:
        # Ensure proper cleanup of MCP client resources when exiting
        await mcp_client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
