from pinecone import init
from langchain.vectorstores.pinecone import Pinecone
from langchain.vectorstores.pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from app.chat.models import ChatArgs
from os import getenv

init(api_key=getenv('PINECONE_API_KEY'),
     environment=getenv('PINECONE_ENV_NAME'))

vector_store = Pinecone.from_existing_index(
    getenv('PINECONE_INDEX_NAME'), OpenAIEmbeddings()
)

def build_retriever(chat_args:ChatArgs, k:int)->VectorStoreRetriever:
    '''
        Builds a Vector DB retriever parameterized with the provided 
        chat's metadata.

        Parameter
        ---------
        `chat_args`: `ChatArgs`
            A Pydantic object holding the chat's metadata.
        `k`: int
            The amount of chunks to be retrieved from the Vector Store.

        Returns
        -------
        A `langchain_core.vectorstores.VectorStoreRetriever` parameterized
        for only retrieving the desired chat's chunks. 
    '''
    search_kwargs = {'filter':{'pdf_id':chat_args.pdf_id}}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
