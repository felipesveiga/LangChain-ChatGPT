from langchain_core.callbacks import BaseCallbackHandler 
from queue import Queue

class StreamingCallback(BaseCallbackHandler):
    '''
        Callback aimed at organizing the streaming of tokens provided by 
        a LLM. 
    '''
    def __init__(self, queue):
        self.queue = queue 
        
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

    def on_llm_end(self, response, **kwargs)->None:
        '''
            Inserts None when the LLM ends its response. 
        '''
        self.queue.put(None)

    def on_llm_error(self, error, **kwargs)->None:
        '''
            Inserts None in the Queue when any error in the LLM's side takes place. 
        '''
        self.queue.put(None)