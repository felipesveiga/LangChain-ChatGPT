from utils._configs import _configs
from typing import Dict, List, Union

def get_configs(module:str)->Dict[str, Dict[str, Union[str, List[str]]]]:
    '''
        Retorna as configurações de um determinado módulo.

        Parâmetro
        ---------
        `module`: str
            Nome do módulo.

        Retorna
        -------
        As configurações das classes do módulo.
    '''
    return _configs[module]