from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from src._prompt import _prompt
from src.tools.tools import *
from src._memory import _memory

tools = [run_query_tool(), describe_tables_tool(), write_csv_tool()]

def _agent()->OpenAIFunctionsAgent:
    '''
        Configures the project's Agent.

        Returns
        -------
        A `langchain.agents.OpenAIFunctionsAgent`

    '''
    global tools
    return OpenAIFunctionsAgent(llm=ChatOpenAI(),
                                prompt=_prompt(),
                                tools=tools
                                )

def agent()->AgentExecutor:
    '''
        Generates the project's Agent Executor.

        Returns
        -------
        A `langchain.agents.OpenAIFunctionsAgent`
    '''
    global tools
    return AgentExecutor(
        agent=_agent(),
        tools=tools,
        memory=_memory(),
        verbose=True
    )