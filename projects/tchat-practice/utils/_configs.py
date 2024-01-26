_configs = {
    'memory':{
        'FileChatMessageHistory':{
            'file_path':'data/messages.json'
        },
        'ConversationBufferMemory':{
            'memory_key':'messages',
            'return_messages':True
        },
    },
    'prompt':{
        'ChatPromptTemplate':{
            'input_variables':['content', 'messages']
        },
        'MessagesPlaceholder':{
            'variable_name':'messages'
        },
        'HumanMessagePromptTemplate':{
            'template':'{content}'
        }
    }
}