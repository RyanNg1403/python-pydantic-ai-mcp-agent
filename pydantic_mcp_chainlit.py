import asyncio
import pathlib
import os
from dotenv import load_dotenv
import chainlit as cl
from typing import List, Dict, Any

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

# Store the agent and client globally to reuse across sessions
agent = None
mcp_client_instance = None

def get_model():
    ollama = OpenAIModel(model_name='mistral', provider=OpenAIProvider(base_url='http://localhost:11434/v1'))
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
    "Be efficient, transparent, and responsive to feedback. "
    "When in doubt, ask the user for clarification."
    )
    return client, Agent(model=get_model(), tools=tools, system_prompt=system_prompt)

def trim_message_history(messages):
    """Trim message history to prevent memory issues in long conversations."""
    if len(messages) <= MAX_HISTORY_LENGTH:
        return messages
    
    # Keep the most recent messages
    return messages[-MAX_HISTORY_LENGTH:]


@cl.on_chat_start
async def on_chat_start():
    global agent, mcp_client_instance
    
    # Initialize the agent if it's not already initialized
    if agent is None:
        try:
            msg = cl.Message(content="Initializing MCP Agent...")
            await msg.send()
            mcp_client_instance, agent = await get_pydantic_ai_agent()
            msg = cl.Message(content="✅ MCP Agent initialized and ready!")
            await msg.send()
        except Exception as e:
            msg = cl.Message(content=f"❌ Failed to initialize MCP Agent: {str(e)}")
            await msg.send()
            raise

    # Store the message history in the user session
    cl.user_session.set("messages", [])

@cl.on_message
async def on_message(message: cl.Message):
    global agent

    # Get the message history from the user session
    messages = cl.user_session.get("messages", [])

    try:
        # Start a new message with a loading state
        with cl.Step(name="Processing with MCP Agent") as step:
            # Process the user input with the agent
            if hasattr(agent, "run") and asyncio.iscoroutinefunction(agent.run):
                result = await agent.run(message.content, message_history=messages)
            elif hasattr(agent, "run_sync"):
                result = agent.run_sync(message.content, message_history=messages)
            else:
                result = agent.run(message.content, message_history=messages)

            # Extract the text content from the result
            result_text = result.data

            # Create an empty message and start streaming
            response_msg = cl.Message(content="")
            await response_msg.send()

            for line in result_text.splitlines(True):  # True keeps the newline characters
                await asyncio.sleep(0.05)  # Delay between lines
                await response_msg.stream_token(line)


            # Finalize the streamed message
            await response_msg.update()

        # Add the new messages to the chat history and trim if needed
        messages.extend(result.all_messages())
        messages = trim_message_history(messages)

        # Update the message history in the user session
        cl.user_session.set("messages", messages)

    except Exception as e:
        # Send an error message
        error_msg = cl.Message(content=f"❌ Error: {str(e)}")
        await error_msg.send()

@cl.on_chat_end
async def on_chat_end():
    global mcp_client_instance
    
    # Clean up MCP client resources when the chat ends
    if mcp_client_instance:
        try:
            await mcp_client_instance.cleanup()
        except Exception as e:
            print(f"Error during MCP client cleanup: {e}")