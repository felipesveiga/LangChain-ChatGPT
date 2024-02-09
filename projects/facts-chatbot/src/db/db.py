from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import RetrievalQA
from src.db.make_docs import make_docs
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
        documents =  make_docs()

        # Criando a DB com os `documents` gerados.
        Chroma.from_documents(documents=documents,
                                    embedding=OpenAIEmbeddings(),
                                    persist_directory='data')

def make_db():
    # Evitando a criação de outro Vector Store.
    if exists('data/'):
        pass
    else:
        _db()
