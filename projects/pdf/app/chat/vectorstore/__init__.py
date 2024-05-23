from functools import partial
from app.chat.vectorstore.pinecone import build_retriever

k_configs = [2,3,5]
retriever_map = {f"pinecone_{k}":partial(build_retriever, k=k) for k in k_configs}