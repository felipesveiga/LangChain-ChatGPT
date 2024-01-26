from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from utils.get_configs import get_configs

def memory()->ConversationBufferMemory:
    '''
        Memória do ChatBot.
    '''
    configs = get_configs('memory')
    chat_memory = FileChatMessageHistory(**configs['FileChatMessageHistory'])
    return ConversationBufferMemory(chat_memory=chat_memory, **configs['ConversationBufferMemory'])