def root_cause_agent(state):
    state["root_cause"] = "Database connection pool exhausted"
    return state
