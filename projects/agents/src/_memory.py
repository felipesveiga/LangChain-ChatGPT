from langchain.memory import ConversationBufferMemory

def _memory()->ConversationBufferMemory:
    '''
        Provides the agent's memory.
    '''
    return ConversationBufferMemory(memory_key='chat_history', return_messages=True)