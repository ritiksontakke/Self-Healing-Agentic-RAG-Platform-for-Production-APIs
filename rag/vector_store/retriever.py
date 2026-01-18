from rag.vector_store.db import get_vector_db

def retrieve_context(query: str, k: int = 3):
    db = get_vector_db()
    docs = db.similarity_search(query, k=k)
    return [d.page_content for d in docs]
