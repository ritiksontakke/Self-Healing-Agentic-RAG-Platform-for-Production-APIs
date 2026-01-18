from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document
from rag.vector_store.db import create_vector_db

documents = [
    Document(page_content="Database connection pool exhaustion causes 500 errors"),
    Document(page_content="Fix DB pool issue by increasing pool size"),
    Document(page_content="Restart service after updating environment variables"),
    Document(page_content="High latency caused by limited DB connections")
]

create_vector_db(documents)
print("✅ Gemini vector store created")
