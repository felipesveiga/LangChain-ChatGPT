from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from src.tools.functions import _list_tables
from src._configs import _configs

_configs = _configs['_prompt']
_configs['SystemMessage']['content'] = _configs['SystemMessage']['content'].format(tables=_list_tables())

def _prompt()->ChatPromptTemplate:
    '''
        Builds our LLM's prompt with the user's request along with the query and its respective output

        Parameter
        ---------
        `human_message`: str
            The human's request.

        Returns
        -------
        A `langchain.prompts.ChatPromptTemplate` with the enlisted messages.
    '''
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessage(**_configs['SystemMessage']),
            MessagesPlaceholder(**_configs['MessagesPlaceholderHistory']),
            HumanMessagePromptTemplate.from_template(**_configs['HumanMessagePromptTemplate']),
            MessagesPlaceholder(**_configs['MessagesPlaceholderScratchpad'])
        ]
    )
    return prompt