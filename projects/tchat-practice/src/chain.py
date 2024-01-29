from src._prompt import prompt
from src._memory import memory
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import LLMChain
from utils.get_configs import get_configs

def chain()->LLMChain:
    configs = get_configs('llm_chain')
    llm = ChatOpenAI()
    return LLMChain(prompt=prompt(), llm=llm, memory=memory(),)