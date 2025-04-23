# Pydantic MCP Agent with Chainlit

A powerful AI agent implementation using Pydantic and Chainlit, capable of web browsing and interaction through MCP (Multi-Command Protocol).

## Features

- Web browsing capabilities with automated interactions
- Integration with Ollama for local LLM support
- Chainlit-based interactive chat interface
- Pydantic models for type-safe data handling
- Configurable MCP server integration

## Prerequisites

- Python 3.8+
- Node.js and npm (for MCP server)
- Ollama installed locally
- MCP server access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RyanNg1403/pydantic-ai-mcp-agent-with-chainlit.git
cd pydantic-ai-mcp-agent-with-chainlit
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Node.js dependencies:
```bash
npm install
```

## Configuration

1. Copy the template configuration file:
```bash
cp mcp_config.template.json mcp_config.json
```

2. Edit `mcp_config.json` with your configuration settings. The file is ignored by git for security.

## Usage

### Running the Chainlit Interface

```bash
chainlit run pydantic_mcp_chainlit.py
```

### Running the Agent Directly

```bash
python pydantic_mcp_agent.py
```

## Project Structure

- `pydantic_mcp_agent.py`: Core agent implementation
- `pydantic_mcp_chainlit.py`: Chainlit interface implementation
- `mcp_client.py`: MCP client implementation
- `requirements.txt`: Python dependencies
- `mcp_config.template.json`: Template for configuration
- `.gitignore`: Specifies which files git should ignore

## Environment Variables

The following environment variables can be set in your `.env` file:

- `EXA_API_KEY`: Your MCP API key
- `OLLAMA_HOST`: Ollama host address (default: http://localhost:11434)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

