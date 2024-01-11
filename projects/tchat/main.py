from langchain.chat_models.ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
def main()->None:
    while True:
        content = input('>> ')
        print(f'Your answer was: {content}')

if __name__=='__main__':
    main()