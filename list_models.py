from dotenv import load_dotenv
load_dotenv()

from google.genai import Client
import os

client = Client(api_key=os.getenv("GOOGLE_API_KEY"))
models = client.list_models()

for m in models:
    print(m.name, m.supported_methods)
