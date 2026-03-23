# secret-agent

A CLI AI coding agent powered by Google Gemini. Given a prompt, the agent plans and executes tasks within a sandboxed working directory using a set of built-in tools.

## Tools

The agent can:
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All file operations are constrained to the configured working directory (`./calculator` by default).

## Setup

1. Install dependencies with [uv](https://github.com/astral-sh/uv):
   ```bash
   uv sync
   ```

2. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_key_here
   ```

## Usage

```bash
uv run main.py "your prompt here"
uv run main.py -v "your prompt here"  # verbose mode
```

The agent runs in a loop (up to 20 iterations) until it produces a final response or exhausts its steps.
