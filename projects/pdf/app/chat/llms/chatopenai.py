from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs

def build_llm(chat_args:ChatArgs)->ChatOpenAI:
    '''
        Builds a conversation's language model instance.
        
        Parameter
        ---------
        `chat_args`: `ChatArgs`
            A Pydantic object holding the chat's metadata.

        Returns
        -------
        An instance of the language model.
    '''
    return ChatOpenAI()