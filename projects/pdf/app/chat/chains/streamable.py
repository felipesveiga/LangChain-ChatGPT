from flask import current_app
from flask.ctx import AppContext
from langchain.chains import LLMChain
from app.chat.callbacks.stream import StreamingCallback
from queue import Queue
from threading import Thread

class StreamableChain:
    def stream(self, input_):
       queue = Queue()
       callback = StreamingCallback(queue)

       def request(app_context:AppContext):
           app_context.push()
           self(input_, callbacks=[callback])
        
       Thread(target=request, args=[current_app.app_context()]).start()
       
       while True:
           token = queue.get()
           if token is None:
              break
           else:
              yield token 