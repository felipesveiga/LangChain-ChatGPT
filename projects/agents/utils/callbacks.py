from typing import Any, Dict, List
from uuid import UUID
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage

class ChatModelStartCallback(BaseCallbackHandler):
    '''
        A basic callback to be used to display the messages list received by the LLM
        previously to its enactment.

        Method
        ------
        `on_chat_model_start`: Displays the list of messages given to the model. 
    '''
    def on_chat_model_start(self, serialized: Dict[str, Any], 
                            messages: List[List[BaseMessage]], 
                            **kwargs: Any) -> None:
        '''
            Displays the list of messages given to the model.

            Parameter
            ---------
            `messages`: List[List[str]]
                The provided batch of messages.
        '''
        print(f'Messages Batch: {messages}')