from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

# Tool input/output models
class ListDocsInput(BaseModel):
    pass

class ListDocsOutput(BaseModel):
    documents: List[str] = Field(description="List of uploaded documents")

class DocAskInput(BaseModel):
    document_name: str = Field(description="Name of the document to query")
    query: str = Field(description="Query to ask about the document")

class DocAskOutput(BaseModel):
    answer: str = Field(description="Answer from the document")

class ListCompaniesInput(BaseModel):
    pass

class ListCompaniesOutput(BaseModel):
    companies: List[str] = Field(description="List of companies in the database")

class AskWebInput(BaseModel):
    query: str = Field(description="Query to search on the web")

class AskWebOutput(BaseModel):
    results: List[str] = Field(description="Web search results")

class ReadWebpageInput(BaseModel):
    url: str = Field(description="URL of the webpage to read")

class ReadWebpageOutput(BaseModel):
    content: str = Field(description="Content of the webpage")

class OperateExcelInput(BaseModel):
    operation: str = Field(description="Excel operation to perform")
    file_name: str = Field(description="Name of the Excel file")
    parameters: Dict[str, Any] = Field(description="Additional parameters for the operation")

class OperateExcelOutput(BaseModel):
    result: str = Field(description="Result of the Excel operation")

class ListTablesInput(BaseModel):
    pass

class ListTablesOutput(BaseModel):
    tables: List[str] = Field(description="List of Excel spreadsheets")

class AskCompanyInput(BaseModel):
    company_name: str = Field(description="Name of the company to query")
    query: str = Field(description="Query about the company")

class AskCompanyOutput(BaseModel):
    answer: str = Field(description="Answer about the company")

# Tool functions
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

# Tool registry for the agent
TOOLS = {
    "list_docs": {
        "function": list_docs,
        "input_model": ListDocsInput,
        "output_model": ListDocsOutput,
        "description": "Lists the user's uploaded documents"
    },
    "doc_ask": {
        "function": doc_ask,
        "input_model": DocAskInput,
        "output_model": DocAskOutput,
        "description": "Brings the document the user wants to query"
    },
    "list_companies": {
        "function": list_companies,
        "input_model": ListCompaniesInput,
        "output_model": ListCompaniesOutput,
        "description": "Lists the companies which are stored in the database"
    },
    "ask_web": {
        "function": ask_web,
        "input_model": AskWebInput,
        "output_model": AskWebOutput,
        "description": "Does a web search on the user's query"
    },
    "read_webpage": {
        "function": read_webpage,
        "input_model": ReadWebpageInput,
        "output_model": ReadWebpageOutput,
        "description": "Reads a webpage the user specifies"
    },
    "operate_excel": {
        "function": operate_excel,
        "input_model": OperateExcelInput,
        "output_model": OperateExcelOutput,
        "description": "Operates an Excel agent (the agent is already defined), this just orchestrates it"
    },
    "list_tables": {
        "function": list_tables,
        "input_model": ListTablesInput,
        "output_model": ListTablesOutput,
        "description": "Lists all the Excel spreadsheets the user has uploaded"
    },
    "ask_company": {
        "function": ask_company,
        "input_model": AskCompanyInput,
        "output_model": AskCompanyOutput,
        "description": "The user queries company specific docs"
    }
}
