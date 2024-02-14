from langchain.chains import RetrievalQA
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models.openai import ChatOpenAI

def chain()->RetrievalQA:
    '''
        Função que gera a chain de chat enriquecido por vectorstore.
    '''
    # Criação do retriver de text chunks.
    retriever = Chroma(persist_directory='data',
                       embedding_function=OpenAIEmbeddings()).as_retriever(k=3)
    
    # Instanciando a chain.
    chain = RetrievalQA.from_chain_type(
                            llm=ChatOpenAI(),
                            retriever=retriever,
                            chain_type='stuff'
                            )
    return chain