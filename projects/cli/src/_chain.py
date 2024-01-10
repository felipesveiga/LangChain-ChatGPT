from langchain.prompts import PromptTemplate
from langchain.llms.openai import OpenAI
from langchain.chains import LLMChain
from typing import Dict, List, Union

def _chain(configs:Dict[str, Union[str, List[str]]])->LLMChain:
    '''
        Template de `LLMChain`s do projeto.

        Parâmetros
        ----------
        `configs`: Dict[str, Union[str, List[str]]]
            Dicionário com as configurações da `LLMChain` dada.
    
        Retorna
        -------
        Um `LLMChain` contendo o `PromptTemplate` e LLM.
    '''
    prompt = PromptTemplate(template=configs['template'],
                        input_variables=configs['input_variables'])
    llm = OpenAI()
    chain= LLMChain(prompt=prompt, llm=llm, output_key=configs['output_key'])
    return chain