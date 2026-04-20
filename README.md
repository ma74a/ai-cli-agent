# AI CLI Agent

A command-line AI coding assistant powered by Google's Gemini API. It uses an agentic loop with function calling to interact with your local filesystem — listing files, reading content, running Python scripts, and writing files.

## Features

- 📂 **List files and directories** — browse your project structure
- 📄 **Read file contents** — inspect any file in the working directory
- ▶️ **Run Python files** — execute scripts with optional arguments
- ✍️ **Write files** — create or overwrite files

The agent runs in a loop, making multiple function calls as needed to fulfill your request before returning a final answer.

## Setup

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager
- A [Gemini API key](https://aistudio.google.com/apikey)

### Installation

```bash
git clone https://github.com/ma74a/ai-cli-agent.git
cd ai-cli-agent
uv sync
```

### Configuration

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

```bash
uv run main.py "your prompt here"
```

### Examples

```bash
# List files in the project
uv run main.py "what files are in the root directory?"

# Read a file
uv run main.py "read the contents of main.py"

# Ask about code
uv run main.py "explain how the calculator works"

# Run with verbose output (shows token usage)
uv run main.py "list all python files" --verbose
```

## Project Structure

```
ai-cli-agent/
├── main.py              # Entry point and agentic loop
├── call_function.py     # Function call dispatcher
├── config.py            # Configuration (working dir, limits)
├── functions/
│   ├── get_files_info.py    # List directory contents
│   ├── get_file_content.py  # Read file contents
│   ├── run_python_file.py   # Execute Python scripts
│   └── write_file.py        # Write/create files
├── pyproject.toml
└── uv.lock
```

## License

MIT
