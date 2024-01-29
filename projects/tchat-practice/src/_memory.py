from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory,FileChatMessageHistory
from langchain.chat_models.openai import ChatOpenAI
from utils.get_configs import get_configs

def memory()->ConversationSummaryMemory:
    '''
        Memória do ChatBot.
    '''
    configs = get_configs('memory')
    llm = ChatOpenAI(**configs['llm'])
    chat_memory = FileChatMessageHistory(**configs['FileChatMessageHistory'])
    return ConversationSummaryMemory(chat_memory=chat_memory, 
                                     llm=llm,
                                     **configs['ConversationSummaryMemory'])