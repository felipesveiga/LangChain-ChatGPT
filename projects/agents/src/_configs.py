_configs = {
    '_prompt':{
        'SystemMessage':{
            'content':'You\'re a SQL analyst whose job is to answer business teams\'s doubts by performing SQL queries. You have the following tables at your disposal: {tables}\n\n Please, utilize the `describe_tables` tool before writing any query. This will furnish you the names of the columns along their respective data type!'
        },
        'MessagesPlaceholderHistory':{
            'variable_name':'chat_history'
        },
        'HumanMessagePromptTemplate':{
            'template':'{input}'
        },
        'MessagesPlaceholderScratchpad':{
            'variable_name':'agent_scratchpad'
        }
    }
    }