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
git clone https://github.com/yourusername/pydantic-ai-mcp-agent.git
cd pydantic-ai-mcp-agent
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install MCP server:
```bash
npm install -g exa-mcp-server
```

## Configuration

1. Copy the template configuration file:
```bash
cp mcp_config.template.json mcp_config.json
```

2. Edit `mcp_config.json` and replace `your-api-key-here` with your actual MCP API key.

## Usage

### Running the Chainlit Interface

```bash
chainlit run pydantic_mcp_chainlit.py
```

### Running the Browser Test

```bash
python browser-use-test/main.py
```

## Project Structure

- `pydantic_mcp_agent.py`: Core agent implementation
- `pydantic_mcp_chainlit.py`: Chainlit interface implementation
- `ollama_model.py`: Ollama LLM integration
- `mcp_client.py`: MCP client implementation
- `browser-use-test/`: Browser automation test examples

## Environment Variables

The following environment variables can be set:

- `EXA_API_KEY`: Your MCP API key
- `OLLAMA_HOST`: Ollama host address (default: http://localhost:11434)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Chainlit team for their excellent chat interface
- Thanks to the Ollama team for their local LLM solution
- Thanks to the MCP team for their browser automation capabilities 