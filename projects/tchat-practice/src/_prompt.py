from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from utils.get_configs import get_configs

def prompt()->ChatPromptTemplate:
    '''
        Montagem do Prompt Template do Chat Bot.
    '''
    configs = get_configs('prompt')
    msg_placeholder = MessagesPlaceholder(**configs['MessagesPlaceholder'])
    msg_human = HumanMessagePromptTemplate.from_template(**configs['HumanMessagePromptTemplate'])
    return ChatPromptTemplate(messages=[msg_placeholder, msg_human], 
                              **configs['ChatPromptTemplate'])