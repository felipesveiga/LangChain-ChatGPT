from langchain.chains import SequentialChain, LLMChain
from src._chain import _chain
from utils._configs import _configs
from typing import List

# configs = _configs
input_chain = _chain(_configs['input_chain'])
test_chain = _chain(_configs['test_chain'])
chains = [input_chain, test_chain]

def main_chain(chains:List[LLMChain]=chains)->SequentialChain:
    '''
        Chain oficial da CLI. Contempla a Chain de geração da função e de teste.

        Parâmetro
        ---------
        `chains`: List[LLMChain]
            Lista contendo as chains do projeto.
        
        Retorna
        -------
        Um objeto `SequentialChain`.
    '''
    configs_main_chain = _configs['main_chain']
    chain = SequentialChain(chains=chains,
                            input_variables=configs_main_chain['input_variables'],
                            output_variables=configs_main_chain['output_variables'])
    return chain
    