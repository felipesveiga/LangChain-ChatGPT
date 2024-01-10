from argparse import ArgumentParser, Namespace
from typing import List

def _args(arguments:List[str])->Namespace:
	'''
		Configura a CLI do projeto, com as variáveis permitidas.

		Parâmetro
		---------
		`arguments`: List[str]
			Lista com o nome dar variáveis da CLI.
		
		Retorna
		-------
		Objeto `Namespace`.
	'''
	parser = ArgumentParser()
	for arg in arguments:
		parser.add_argument(arg)
	args = parser.parse_args()
	return args
