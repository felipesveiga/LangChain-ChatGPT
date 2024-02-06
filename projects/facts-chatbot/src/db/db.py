from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from src.db.make_docs import make_docs

def db()->None:
    '''
        Função para a criação de um Vector Store para o projeto.
    '''
    # Gerando o embedding de 'hello, world'.
    embeddings = OpenAIEmbeddings()
    
    # Invocando os `Documents` do projeto que vão ser convertidos em Embeddings.
    documents =  make_docs()

    chroma = Chroma.from_documents(documents=documents,
                                   embedding=embeddings,
                                   persist_directory='data')