from langchain.tools import Tool, StructuredTool
from src.tools.functions import *
from src.tools._args_schemas import *
from typing import Callable, Any
from pydantic.v1 import BaseModel

def _make_tool(description:str, func:Callable[[Any], Any], args_schema:BaseModel, multiple_args:bool=False)->Tool:
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
        `multiple_args`: bool
            Whether the provided method has multiple arguments.
        
        Returns
        -------
        A `langchain.tools.Tool` based on a given method.
    '''
    name = func.__name__ # Defining the function's name to be informed to the `Tool` object.
    tool = StructuredTool if multiple_args else Tool
    tool = tool.from_function(
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

def write_csv_tool()->StructuredTool:
    description = 'Writes a query and its output into a .csv file. Only use this if the user has demanded such execution!'
    return _make_tool(description=description, func=write_csv, args_schema=WriteCSVSchema, multiple_args=True)