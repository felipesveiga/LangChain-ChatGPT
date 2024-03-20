from langchain.tools import Tool
from src.tools.functions import run_query, describe_tables
from src.tools._args_schemas import DescribeTablesSchema, RunQuerySchema
from typing import Callable, Any
from pydantic.v1 import BaseModel

def _make_tool(description:str, func:Callable[[Any], Any], args_schema:BaseModel)->Tool:
    '''
        Generates an object `langchain.tools.Tool` based on a provided method.

        Parameters
        ----------
        `description`: str
            The function's description
        `func`: Callable[[Any], Any]
            The function to be treated.
        `args_schema`: BaseModel
            A class represeting the tool's schema.
        
        Returns
        -------
        A `langchain.tools.Tool` based on a given method.
    '''
    name = func.__name__ # Defining the function's name to be informed to the `Tool` object.
    tool = Tool.from_function(
        name=name,
        description=description,
        func=func,
        args_schema=args_schema
    )
    return tool

def describe_tables_tool()->Tool:
    description = 'Provides the schema of the desired tables'
    return _make_tool(description=description, func=describe_tables, args_schema=DescribeTablesSchema)

def run_query_tool()->Tool:
    '''
        Returns an object `langchain.tools.Tool` related to the funtion the 
        `src.tools.functions.run_query`.
    '''
    description = 'Performs an SQLite query'
    return _make_tool(description=description, func=run_query, args_schema=RunQuerySchema)
