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

### Testing
```bash
python test_orchestrator.py
```
