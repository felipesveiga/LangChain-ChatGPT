from langchain.embeddings.base import Embeddings
from langchain.vectorstores.chroma import Chroma
from langchain.schema import BaseRetriever

class FilterRetriever(BaseRetriever):
    '''
        Retriever que faz filtragem de embeddings redundantes.

        Parâmetro
        ---------
        `embeddigs`: `Embeddings`
            Classe de modelo de Embeddigs.
        `chroma`: `Chroma`
            Instância configurada da classe `Chroma`, preparada para queries na DB.
        `lambda_mult`: int
            Float que ajustará a rigidez da filtragem. Quanto maior for, menos documentos
            redundantes serão retornados.
        
        Método
        -------
        `get_relevant_documents`: Realiza a query filtrada na Vectorstore.
    '''
    embeddings:Embeddings
    chroma: Chroma
    lambda_mult: int=.8

    def get_relevant_documents(self, query:str):
        emb = self.embeddings.embed_query(query)
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=self.lambda_mult
        )
    
    async def aget_relevant_documents(self):
        return []
