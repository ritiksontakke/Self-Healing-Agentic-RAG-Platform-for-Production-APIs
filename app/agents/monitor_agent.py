def monitor_agent(state):
    state["error_log"] = state.get(
        "error_log",
        "500 error on /payments endpoint"
    )
    return state
