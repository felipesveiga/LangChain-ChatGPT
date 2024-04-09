from pinecone import init
from langchain.vectorstores.pinecone import Pinecone
from langchain.vectorstores.pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from os import getenv

init(api_key=getenv('PINECONE_API_KEY'),
     environment=getenv('PINECONE_ENV_NAME'))

vector_store = Pinecone.from_existing_index(
    getenv('PINECONE_INDEX_NAME'), OpenAIEmbeddings()
)

vector_store.as_retriever()