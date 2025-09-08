# PyKy - AI Code Assistant

PyKy is a Python-based AI coding assistant that leverages Google's Gemini 2.0 Flash model to help with code analysis, debugging, and development tasks. It provides an interactive command-line interface where you can ask questions about code and get intelligent assistance with file operations within a sandboxed working directory.

## Features

- **AI-Powered Code Analysis**: Uses Google Gemini 2.0 Flash for intelligent code understanding and assistance
- **Secure File Operations**: Sandboxed file system access limited to a designated working directory
- **Function Calling**: Integrates with Gemini's function calling capabilities for structured operations
- **Interactive CLI**: Simple command-line interface for natural language coding queries

### Available Operations

- **File Listing**: Browse files and directories with size information
- **File Reading**: Read file contents (up to 10,000 characters)
- **Python Execution**: Run Python scripts with arguments and capture output
- **File Writing**: Create and modify files within the working directory

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pyky
```

2. Install dependencies using [uv](https://github.com/astral-sh/uv):
```bash
uv sync
```

Or with pip:
```bash
pip install google-genai python-dotenv
```

3. Set up your Google AI API key:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
GEMINI_API_KEY=your-api-key-here
```

## Usage

Run PyKy with a natural language prompt:

```bash
python main.py "your question or request here"
```

### Examples

```bash
# Ask about code issues
python main.py "How do I fix the calculator?"

# Request code analysis
python main.py "Review the calculator code for potential bugs"

# Get help with implementation
python main.py "Add error handling to the main function"

# Enable verbose output
python main.py "Explain what the calculator does" --verbose
```

## Configuration

- `MAX_CHARS`: Maximum characters to read from files (default: 10,000)
- `WORKING_DIR`: Sandboxed directory for file operations (default: "./calculator")

## Example Project

The repository includes a sample calculator project in the `calculator/` directory that demonstrates:

- Basic arithmetic operations (+, -, *, /)
- Expression parsing with operator precedence
- Pretty-printed output with Unicode box drawing
- Error handling for invalid expressions

Run the calculator example:
```bash
cd calculator
python main.py "3 + 5 * 2"
```

## Project Structure

```
pyky/
├── main.py              # Main CLI entry point
├── call_function.py     # Function calling orchestration
├── prompts.py          # System prompts for the AI
├── config.py           # Configuration settings
├── functions/          # Available AI functions
│   ├── get_file_content.py    # File reading
│   ├── get_files_info.py      # Directory listing
│   ├── run_python.py          # Python execution
│   └── write_file_content.py  # File writing
└── calculator/         # Example project
    ├── main.py
    ├── pkg/
    │   ├── calculator.py
    │   └── render.py
    └── tests.py
```

## Security

PyKy implements several security measures:

- **Sandboxed file access**: All file operations are restricted to the configured working directory
- **Path validation**: Prevents directory traversal attacks
- **Execution timeout**: Python script execution is limited to 30 seconds
- **Input validation**: File paths and arguments are validated before execution

## Dependencies

- **google-genai**: Google's Gemini AI SDK
- **python-dotenv**: Environment variable management
- **Python 3.13+**: Modern Python features and performance

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

Contributions are welcome! Please ensure all changes maintain the security boundaries and follow the existing code structure.