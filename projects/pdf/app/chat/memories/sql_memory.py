from langchain.memory import ConversationBufferMemory
from langchain_core.chat_history import BaseChatMessageHistory
from pydantic import BaseModel
from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)
from app.web.db.models import Message
from langchain_core.messages import BaseMessage
from app.chat.models import ChatArgs

class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str

    @property
    def messages(self):
        '''
            Retrieves a given conversation's chat history.
        '''
        return get_messages_by_conversation_id(self.conversation_id)
    
    def add_message(self, message:BaseMessage)->Message:
        '''
            Adds a new message to a chat history.

            Parameters
            ----------
            `message`: `langchain_core.BaseMessage`
                The message to be added.

            Returns
            -------
            A `Message` object with the provided `message` metadata.
        '''
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message
        )
    
    def clear(self):
        pass

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