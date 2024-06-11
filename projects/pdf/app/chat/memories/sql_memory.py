from langchain.memory import ConversationBufferMemory
from langchain_core.messages import BaseMessage

def build_memory(chat_args:ChatArgs)->ConversationBufferMemory:
    '''
        Builds a conversation's memory.
        
        Parameter
        ---------
        `chat_args`: `ChatArgs`
            A Pydantic object holding the chat's metadata.

        Returns
        -------
        A `langchain.memory.ConversationBufferMemory` parameterized 
        with the chat's data.
    '''
    sql_message_history = SqlMessageHistory(conversation_id=chat_args.conversation_id)
    return ConversationBufferMemory(
        chat_memory=sql_message_history,
        return_messages=True,
        memory_key='chat_history',
        output_key='answer'
    )