from langchain.memory import ConversationBufferWindowMemory
from app.chat.memories.histories.sql_history import SqlMessageHistory
from app.chat.models import ChatArgs

def window_buffer_memory_builder(chat_args:ChatArgs)->ConversationBufferWindowMemory:
    '''
        Builds a conversation's memory.
        
        Parameter
        ---------
        `chat_args`: `ChatArgs`
            A Pydantic object holding the chat's metadata.

        Returns
        -------
        A `langchain.memory.ConversationBufferWindowMemory` parameterized 
        with the chat's data
    '''
    sql_message_history = SqlMessageHistory(conversation_id=chat_args.conversation_id)
    return ConversationBufferWindowMemory(
        chat_memory=sql_message_history,
        return_messages=True,
        memory_key='chat_history',
        output_key='answer',
        k=2) 