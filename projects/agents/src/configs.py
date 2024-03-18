_configs = {
    '_prompt':{
        'SystemMessage':{
            'content':'You\'re a SQL analyst whose job is to answer business teams\'s doubts by performing SQL queries. You have the following tables at your disposal: {tables}\n\n Please, utilize the provided tools. Avoid disregarding them during your tasks\' execution!!'
        },
        'HumanMessagePromptTemplate':{
            'template':'{human_message}'
        },
        'MessagesPlaceholder':{
            'variable_name':'agent_scratchpad'
        }
    }
    }