from src.agent import agent

def main()->None:
    user_message = input('>>')
    ai_agent = agent()
    print(ai_agent.invoke(user_message))
    #print(ai_agent.invoke('How much is that last number you\'ve outputed minus 200? '))
    # How many clients we have? Insert the output in the data/hi.csv file

if __name__=='__main__':
    main()