from sqlite3 import connect, OperationalError
from typing import List

def run_query(query:str, database:str='../../assets/06_db.sqlite')->List[str]:
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