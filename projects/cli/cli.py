from langchain.prompts import PromptTemplate
from langchain.llms.openai import OpenAI
from langchain.chains import LLMChain
from utils._parser import _args

def main():
    '''
        Executa a CLI, fazendo uma requisição à OpenAI e retornando seu output.
    '''
    args = _args(['--language', '--task'])

    # Prompt Template a ser encaminhado à OpenAI
    prompt = PromptTemplate(template='Write a short {language} function that will {task}',
                        input_variables=['language', 'task']
                        )
    # Classe do LLM.
    llm = OpenAI() 

    # Instanciando a Chain da CLI e invocando-a com os argumentos do usuário.
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain(inputs={
        'language':args.language,
        'task':args.task
    })

    print(result['text'])

if __name__ == '__main__':
    main()