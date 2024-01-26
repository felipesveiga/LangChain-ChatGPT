from src.chain import chain

def main():
    while True:
        content = input('>> ')
        result = chain()(inputs={
            'content':content
        })['text']
        print(f'Open AI: {result}')

if __name__ == '__main__':
    main()