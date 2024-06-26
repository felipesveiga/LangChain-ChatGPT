from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from app.chat.utils import _builder
from app.chat.llms.chatopenai import build_llm
from app.chat.vectorstore.pinecone import build_retriever
from app.chat.memories.sql_memory import build_memory
from app.chat.models import ChatArgs
from app.chat.tracing.langfuse import langfuse
from langfuse.model import CreateTrace

def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    llm, retriever, memory = _builder(chat_args)
    condense_question_llm = ChatOpenAI(streaming=False)

    trace = langfuse.trace(
        CreateTrace(
            id=chat_args.conversation_id,
            metadata=chat_args.metadata
        )
    )
    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=retriever,
        condense_question_llm=condense_question_llm,
        callbacks=[trace.getNewHandler()]
    )