from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.chains import LLMChain

def main()->None:
    prompt = ChatPromptTemplate(
        input_variables=['content'],
        messages=[
            HumanMessagePromptTemplate.from_template('{content}')
        ]
    )

    llm = ChatOpenAI()
    chain = LLMChain(prompt=prompt, llm=llm)

    while True:
        content = input('>>')
        result = chain(inputs={
            'content':content
        })['text']
        print(f'Open AI: {result}')

if __name__=='__main__':
    main()