from src.main_chain import main_chain
from utils._parser import _args
from utils._configs import _configs

configs = _configs['cli']

def main():
    '''
        Executa a CLI, fazendo uma requisição à OpenAI e retornando seu output.
    '''
    args = _args(configs['arguments'])
    chain = main_chain()
    results = chain(inputs={
        'task':args.task,
        'language':args.language
    })
    print(results)

if __name__ == '__main__':
    main()