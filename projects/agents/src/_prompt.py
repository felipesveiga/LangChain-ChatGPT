from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

def _prompt(human_message:str)->ChatPromptTemplate:
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
            HumanMessagePromptTemplate.from_template(f'{human_message}'),
            MessagesPlaceholder(variable_name='agent_scratchpad')
        ]
    )
    return prompt