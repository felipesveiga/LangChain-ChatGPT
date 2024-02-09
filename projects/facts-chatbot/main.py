from src.chain import chain
from src.db.db import make_db

def main():
    # Criação condicional da vector store.
    make_db() 

    # User prompt.
    content = input('>> ')
    result = chain()(content)['result']

    # Retorno OpenAI.
    print(f'OpenAI: {result}')

if __name__ == '__main__':
    main()