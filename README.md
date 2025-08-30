# Main Orchestrator Agent

A Pydantic AI-powered agent that orchestrates various tools to handle user queries intelligently using AWS Bedrock.

## 🚀 Features

The agent has access to 8 main tools:

1. **`list_docs`** - Lists user's uploaded documents
2. **`doc_ask`** - Queries specific documents
3. **`list_companies`** - Lists companies stored in the database
4. **`ask_web`** - Performs web searches
5. **`read_webpage`** - Reads webpage content
6. **`operate_excel`** - Orchestrates Excel operations
7. **`list_tables`** - Lists Excel spreadsheets
8. **`ask_company`** - Queries company-specific documents

## 🏗️ Architecture

- **Main Agent**: Orchestrates all tools and determines which ones to use based on user queries
- **Tools Module**: Contains all tool definitions with proper input/output models
- **AWS Bedrock Integration**: Uses Claude Sonnet 4 for intelligent decision making

## 📋 Requirements

- Python 3.8+
- AWS credentials configured
- Access to the specified Bedrock model

## 🛠️ Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your configuration:
```bash
BEDROCK_CLAUDE_MODEL=bedrock:us.anthropic.claude-sonnet-4-20250514-v1:0
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
```

3. Configure AWS credentials (if not already done):
```bash
aws configure
```

## 🚀 Usage

### Interactive Mode
```bash
python orchestrator.py
```

### Testing
```bash
python test_orchestrator.py
```

## 🔧 Configuration

The agent is configured to use environment variables from a `.env` file:
- **BEDROCK_CLAUDE_MODEL**: Set in your `.env` file
- **Region**: `us-east-1` (configurable via AWS_REGION env var)

## 🎯 Example Queries

- "List all companies" → Calls `list_companies` tool
- "What documents do I have?" → Calls `list_docs` tool
- "Search for AI trends" → Calls `ask_web` tool
- "Read https://example.com" → Calls `read_webpage` tool
- "Analyze my sales data" → Calls `operate_excel` tool

## 📁 File Structure

```
.
├── orchestrator.py      # Main agent implementation
├── tools.py            # Tool definitions and models
├── test_orchestrator.py # Testing script
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## 🔒 Security Notes

⚠️ **IMPORTANT**: This agent is configured for production use. Always verify:
- Correct AWS credentials and permissions
- Production-ready configurations
- Security best practices
