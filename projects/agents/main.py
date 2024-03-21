from src.agent import agent

def main()->None:
    user_message = input('>>')
    print(agent().invoke(user_message))
    # How many clients we have? Insert the output in the data/hi.csv file

if __name__=='__main__':
    main()