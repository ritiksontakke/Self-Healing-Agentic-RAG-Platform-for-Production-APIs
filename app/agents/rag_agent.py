from rag.vector_store.retriever import retrieve_context

def rag_agent(state):
    query = state.get("root_cause", "")
    state["rag_context"] = retrieve_context(query, k=3)
    return state
