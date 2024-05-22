from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs

def build_llm(chat_args:ChatArgs, model_name:str)->ChatOpenAI:
    '''
        Builds a conversation's language model instance.
        
        Parameter
        ---------
        `chat_args`: `ChatArgs`
            A Pydantic object holding the chat's metadata.
        `model_name`: str
            The name of the model to be used.

        Returns
        -------
        An instance of the language model.
    '''
    return ChatOpenAI(streaming=chat_args.streaming, model_name=model_name)