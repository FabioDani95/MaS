"""Workflow orchestration for agent execution."""

from agents.extractor_agent import extractor_agent
from agents.resolver_agent import resolver_agent
from agents.router_agent import router_agent
from state import WorkflowState


def run_workflow(state: WorkflowState) -> WorkflowState:
    """Run agents in sequence: router -> extractor -> resolver."""

    state = router_agent(state)
    state = extractor_agent(state)
    state = resolver_agent(state)
    return state
