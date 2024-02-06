from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain_core.documents import Document
from typing import List

def make_docs(file_path:str='../../assets/04_facts.txt')->List[Document]:
    '''
        Função que cria os text chunks do projeto.
    '''
    splitter = CharacterTextSplitter(separator='\n',
                                            chunk_size=200,
                                            chunk_overlap=0)

    # Dividindo o texto.
    docs = TextLoader(file_path).load_and_split(splitter)
    return docs