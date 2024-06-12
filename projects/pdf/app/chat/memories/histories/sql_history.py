from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)
from app.web.db.models import Message
from app.chat.models import ChatArgs
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from pydantic import BaseModel

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
            content=message.content
        )
    
    def clear(self):
        pass

