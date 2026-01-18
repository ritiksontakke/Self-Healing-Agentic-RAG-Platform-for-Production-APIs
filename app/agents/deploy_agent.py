def deploy_agent(state):
    state["deployment_status"] = "PR created – waiting for approval"
    return state
