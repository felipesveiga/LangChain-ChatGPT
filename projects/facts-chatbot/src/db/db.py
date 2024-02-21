from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from src.db._make_docs import _make_docs
from os.path import exists

def _db()->None:
    '''
        Função para a criação de um Vector Store para o projeto.
    '''
    # Controlando 
    if exists('data/'):
        pass
    else:
        # Invocando os `Documents` do projeto que vão ser convertidos em Embeddings.
        documents =  _make_docs()

        # Criando a DB com os `documents` gerados.
        Chroma.from_documents(documents=documents,
                                    embedding=OpenAIEmbeddings(),
                                    persist_directory='data')

def make_db():
    '''
        Cria a Vectorstore apenas quando o diretório 'data' não está
        presente.
    '''
    # Evitando a criação de outro Vector Store.
    if exists('data/'):
        pass
    else:
        _db()
