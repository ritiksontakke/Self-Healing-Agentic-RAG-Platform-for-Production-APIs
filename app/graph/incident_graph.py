from langgraph.graph import StateGraph
from app.agents.monitor_agent import monitor_agent
from app.agents.root_cause_agent import root_cause_agent
from app.agents.rag_agent import rag_agent
from app.agents.fix_agent import fix_agent
from app.agents.deploy_agent import deploy_agent

graph = StateGraph(dict)

graph.add_node("monitor", monitor_agent)
graph.add_node("root_cause", root_cause_agent)
graph.add_node("rag", rag_agent)
graph.add_node("fix", fix_agent)
graph.add_node("deploy", deploy_agent)

graph.set_entry_point("monitor")

graph.add_edge("monitor", "root_cause")
graph.add_edge("root_cause", "rag")
graph.add_edge("rag", "fix")

graph.add_conditional_edges(
    "fix",
    lambda state: "deploy" if state["confidence"] > 0.8 else "monitor"
)

incident_graph = graph.compile()
