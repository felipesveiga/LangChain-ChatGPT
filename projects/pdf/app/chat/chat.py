from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from app.chat.llms.chatopenai import build_llm
from app.chat.vectorstore.pinecone import build_retriever
from app.chat.memories.sql_memory import build_memory
from app.chat.models import ChatArgs


def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    llm = build_llm(chat_args)
    condense_question_llm = ChatOpenAI(streaming=False)
    retriever = build_retriever(chat_args)
    memory = build_memory(chat_args)
    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=retriever,
        condense_question_llm=condense_question_llm
    )