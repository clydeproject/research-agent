import os
import json
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from pydantic_ai import Agent, Tool
from pydantic_ai.models import infer_model
from pydantic_ai.providers.bedrock import BedrockProvider
from dotenv import load_dotenv
from tools import TOOLS

# Load environment variables
load_dotenv()

# Configure AWS Bedrock model from environment
LLM_MODEL = os.getenv("BEDROCK_CLAUDE_MODEL")
if not LLM_MODEL:
    raise ValueError("BEDROCK_CLAUDE_MODEL environment variable not set. Please check your .env file.")

# Get AWS region from environment or default to us-east-1
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Set AWS region in environment for Bedrock
os.environ["AWS_DEFAULT_REGION"] = AWS_REGION

# Initialize the LLM using infer_model
llm = infer_model(LLM_MODEL)

# Create tool instances for the agent
def list_docs() -> str:
    """Lists the user's uploaded documents"""
    return "list_docs tool called"

def doc_ask(document_name: str, query: str) -> str:
    """Brings the document the user wants to query"""
    return f"doc_ask tool called with document: {document_name}, query: {query}"

def list_companies() -> str:
    """Lists the companies which are stored in the database"""
    return "list_companies tool called"

def ask_web(query: str) -> str:
    """Does a web search on the user's query"""
    return f"ask_web tool called with query: {query}"

def read_webpage(url: str) -> str:
    """Reads a webpage the user specifies"""
    return f"read_webpage tool called with URL: {url}"

def operate_excel(operation: str, file_name: str, parameters: Dict[str, Any]) -> str:
    """Operates an Excel agent (the agent is already defined), this just orchestrates it"""
    return f"operate_excel tool called with operation: {operation}, file: {file_name}, parameters: {parameters}"

def list_tables() -> str:
    """Lists all the Excel spreadsheets the user has uploaded"""
    return "list_tables tool called"

def ask_company(company_name: str, query: str) -> str:
    """The user queries company specific docs"""
    return f"ask_company tool called with company: {company_name}, query: {query}"

# Create the main orchestrator agent
class MainAgent:
    def __init__(self):
        self.agent = Agent(
            model=llm,
            tools=[
                Tool(list_docs),
                Tool(doc_ask),
                Tool(list_companies),
                Tool(ask_web),
                Tool(read_webpage),
                Tool(operate_excel),
                Tool(list_tables),
                Tool(ask_company)
            ],
            system_prompt="""You are an intelligent AI agent that orchestrates various tools to help users with their queries. 
            
            Available tools:
            - list_docs: Lists uploaded documents
            - doc_ask: Queries specific documents
            - list_companies: Lists companies in the database
            - ask_web: Performs web searches
            - read_webpage: Reads webpage content
            - operate_excel: Operates Excel files
            - list_tables: Lists Excel spreadsheets
            - ask_company: Queries company-specific documents
            
            When a user asks a question, determine which tool(s) would be most appropriate and use them to provide a helpful response.
            Always explain what you're doing and provide clear, actionable information.
            
            IMPORTANT: Always use the appropriate tools when the user asks for specific information. Don't just describe what you would do - actually execute the tools and provide the results."""
        )
    
    def process_query_sync(self, user_query: str) -> str:
        """Synchronous version of process_query for testing"""
        try:
            import asyncio
            
            # Create a new event loop for this thread
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            # Run the async agent
            response = loop.run_until_complete(self.agent.run(user_query))
            
            # Get all messages to see tool calls
            all_messages = response.all_messages()
            
            # Find tool calls and their outputs
            tool_calls = []
            for message in all_messages:
                if hasattr(message, 'parts'):
                    for part in message.parts:
                        if hasattr(part, 'tool_name'):
                            tool_calls.append({
                                'name': part.tool_name,
                                'args': getattr(part, 'args', {}),
                                'content': getattr(part, 'content', '')
                            })
            
            # Display tool calls if any
            if tool_calls:
                print("\nTools called:")
                for tool in tool_calls:
                    print(f"- {tool['name']}: {tool['content']}")
            
            # Return the final response
            if hasattr(response, 'output'):
                return str(response.output)
            else:
                return str(response)
                
        except Exception as e:
            return f"Error: {str(e)}"

# Create a simple CLI interface for testing
def main():
    agent = MainAgent()    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            if not user_input:
                continue
            
            # Process the query
            response = agent.process_query_sync(user_input)
            print(f"Agent: {response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
