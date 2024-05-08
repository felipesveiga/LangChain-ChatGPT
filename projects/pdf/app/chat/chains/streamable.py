from langchain.chains import LLMChain
from app.chat.callbacks.stream import StreamingCallback
from queue import Queue
from threading import Thread

class StreamableChain:
    def stream(self, input_):
       queue = Queue()
       callback = StreamingCallback(queue)

       def request():
           self(input_, callbacks=[callback])
        
       Thread(target=request).start()
       
       while True:
           token = queue.get()
           if token is None:
              break
           else:
              yield token 