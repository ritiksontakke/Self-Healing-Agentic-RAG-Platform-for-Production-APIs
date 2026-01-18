import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_vector_db():
    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=GOOGLE_API_KEY
        )
    )

def create_vector_db(documents):
    db = Chroma.from_documents(
        documents,
        GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=GOOGLE_API_KEY
        ),
        persist_directory=VECTOR_DB_PATH
    )
    db.persist()
    return db
