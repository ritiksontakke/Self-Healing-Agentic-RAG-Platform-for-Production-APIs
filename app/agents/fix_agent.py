import os
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)

def fix_agent(state):
    prompt = f"""
    Incident: {state.get("root_cause")}
    Context: {state.get("rag_context")}

    Suggest a safe production fix with rollback.
    """

    response = llm.invoke(prompt)
    state["suggested_fix"] = response.content
    state["confidence"] = 0.9
    return state
