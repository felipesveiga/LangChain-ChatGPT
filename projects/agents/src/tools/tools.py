from langchain.tools import Tool
from src.tools.functions import run_query, describe_tables
from typing import Callable, Any

def _make_tool(description:str, func:Callable[[Any], Any])->Tool:
    '''
        Generates an object `langchain.tools.Tool` based on a provided method.

        Parameters
        ----------
        `description`: str
            The function's description
        `func`: Callable[[Any], Any]
            The function to be treated.
        
        Returns
        -------
        A `langchain.tools.Tool` based on a given method.
    '''
    name = func.__name__ # Defining the function's name to be informed to the `Tool` object.
    tool = Tool.from_function(
        name=name,
        description=description,
        func=func
    )
    return tool

def run_query_tool()->Tool:
    '''
        Returns an object `langchain.tools.Tool` related to the funtion the 
        `src.tools.functions.run_query`.
    '''
    descripton = 'Performs an SQLite query'
    return _make_tool(descripton=descripton, func=run_query)

def describe_tables_tool()->Tool:
    description = 'Provides the schema of the desired tables'
    return _make_tool(description=description, func=describe_tables)