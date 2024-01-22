from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory

def main()->None:
    chat_memory = FileChatMessageHistory('data/messages.json')

    memory = ConversationBufferMemory(chat_memory=chat_memory,
                                      memory_key='messages', 
                                      return_messages=True)
    prompt = ChatPromptTemplate(
        input_variables=['content', 'messages'],
        messages=[
            MessagesPlaceholder(variable_name='messages'), 
            HumanMessagePromptTemplate.from_template('{content}')
        ]
    )

    llm = ChatOpenAI()
    chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

    while True:
        content = input('>> ')
        result = chain(inputs={
            'content':content
        })['text']
        print(f'Open AI: {result}')

if __name__=='__main__':
    main()