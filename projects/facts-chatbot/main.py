from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

# Gerando o embedding de 'hello, world'.
embeddings = OpenAIEmbeddings()
emb = embeddings.embed_query('hello, world')
#embeddings.embed_query()
# Invocando o splitter do projeto.
splitter = CharacterTextSplitter(separator='\n',
                                 chunk_size=200,
                                 chunk_overlap=0)

# Dividindo o texto.
content = TextLoader('../../assets/04_facts.txt').load_and_split(splitter)
print(emb)