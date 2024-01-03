from langchain.llms.openai import OpenAI

llm = OpenAI() # Classe do modelo.
result = llm('Tell me about LangChain') # Resultado da consulta.
print(result)