from typing import Any, Dict, List
from uuid import UUID
from langchain_core.callbacks import BaseCallbackHandler 
from queue import Queue

from langchain_core.messages import BaseMessage

class StreamingCallback(BaseCallbackHandler):
    '''
        Callback aimed at organizing the streaming of tokens provided by 
        a LLM. 
    '''
    def __init__(self, queue:Queue):
        self.queue = queue 
        self.streaming_ids = set()

    def on_chat_model_start(self, serialized: Dict[str, Any], messages: List[List[BaseMessage]], *, run_id: UUID, **kwargs: Any) -> Any:
        '''
            Registers the model's run id if it enables streaming.

            Parameter
            ---------
            `run_id`: str
                The run id.
        '''
        if serialized['kwargs']['streamiing']:
            self.streaming_ids.add(run_id)
        
    def on_llm_new_token(self, token:str, **kwargs)->None:
        '''
            Encharged with inserting a new token on the callback's queue.

            Parameters
            ----------
            `token`: str
                The LLM's generated token.
            `**kwargs`: Any additional key-word argument (it is not going to be
            used by the callback).
        '''
        self.queue.put(token)

    def on_llm_end(self, response, run_id, **kwargs)->None:
        '''
            Inserts None when the LLM ends its response. 
        '''
        if run_id in self.streaming_ids: 
            self.queue.put(None)
            self.streaming_ids.remove(run_id)

    def on_llm_error(self, error, **kwargs)->None:
        '''
            Inserts None in the Queue when any error in the LLM's side takes place. 
        '''
        self.queue.put(None)