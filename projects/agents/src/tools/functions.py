from sqlite3 import connect, OperationalError
from typing import List
from src.tools.configs import _configs

_configs = _configs['functions']
database = _configs['database']

def _list_tables()->str:
    '''
        Provides the names of the database's tables.
    '''
    conn = connect(database)
    cursor = conn.cursor()
    outputs = cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\';')
    return ', '.join([output[0] for output in outputs])

def describe_tables(table_names:List[str])->str:
    '''
        Executes a query demanding the schema of the provided tables.

        Parameter
        --------
        `table_names`: List[str]
            A list with the names of the desired tables.

        Returns
        -------
        The description of the tables in a string.
    '''
    tables = ', '.join([f'\'{table}\'' for table in table_names])
    conn = connect(database)
    cursor = conn.cursor()
    outputs = cursor.execute(**_configs['describe_tables']['execute'].format(tables=tables))
    return '\n'.join(description[0] for description in outputs if description[0] is not None)

def run_query(query:str)->List[str]:
    '''
        Runs a provided query on a database.

        Parameters
        ----------
        `query`: str
            Query text.
        `database`: str
            Path to the SQLite database.

        Returns
        -------
        A list containing the query outputs.
    '''
    conn = connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except OperationalError as err:
        return f'The following error occurred whilst executing your query: \n {err}'