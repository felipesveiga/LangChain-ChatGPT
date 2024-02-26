from langchain.chains import RetrievalQA
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models.openai import ChatOpenAI
from src.db._retriever import FilterRetriever

def chain()->RetrievalQA:
    '''
        Função que gera a chain de chat enriquecido por vectorstore.
    '''
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    # Criação do retriver de text chunks.
    chroma = Chroma(persist_directory='data',
                       embedding_function=embeddings)
    
    retriever = FilterRetriever(embeddings=embeddings,
                                chroma=chroma,
                                lambda_mult=.8)
    # Instanciando a chain.
    chain = RetrievalQA.from_chain_type(
                            llm=llm,
                            retriever=retriever,
                            chain_type='stuff'
                            )
    return chain