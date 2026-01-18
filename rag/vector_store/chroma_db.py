from langchain_community.vectorstores import Chroma
from rag.vector_store.embeddings import get_embeddings

def get_vectorstore(persist_dir="data/chroma"):
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )
