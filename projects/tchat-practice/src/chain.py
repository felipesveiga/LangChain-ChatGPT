from src._prompt import prompt
from src._memory import memory
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import LLMChain

def chain()->LLMChain:
    llm = ChatOpenAI()
    return LLMChain(prompt=prompt(), llm=llm, memory=memory())