from utils._configs import _configs
from typing import Dict, List, Union

def get_configs(module:str)->Dict[str, Dict[str, Union[str, List[str]]]]:
    '''
        Returns the configurations of the objects from a given module.
        
        Parameter
        ---------
        `module`: str
            Module's name.

        Returns
        -------
        The configurations of the objects
    '''
    return _configs[module]