from pydantic.v1 import BaseModel
from typing import List

class DescribeTablesSchema(BaseModel):
    '''
        Schema for the `describe_tables_tool`.
    '''
    table_names: List[str]

class RunQuerySchema(BaseModel):
    '''
        Schema for the `run_query_tool`.
    '''
    query: str