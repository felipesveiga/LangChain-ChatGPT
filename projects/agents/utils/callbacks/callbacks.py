from typing import Any, Dict, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from pyboxen import boxen
from utils.callbacks._configs import _configs_boxen

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
        for message in messages[0]:
            if message.type=='system':
                boxen(message.content, title=message.type, **_configs_boxen['system'])
            elif message.type=='human':
                boxen(message.content, title=message.type, **_configs_boxen['human'])
            elif message.type=='ai':
                if 'function_call' in message.additional_kwargs:
                    boxen(title=message.type, **_configs_boxen['ai-function'])
                else:
                    boxen(message.content, title=message.type, **_configs_boxen['ai'])
            elif message.type=='function':
                boxen(message.content, title=message.type, **_configs_boxen['function'])
            else:
                boxen(message.content, title=message.type, **_configs_boxen['else'])
            