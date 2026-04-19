# verified: 2026-04-17 · TDD × Bridle · starter tests steer the agent before it writes
"""A minimal failing-first suite that pins the agent loop shape.

Committing this file before the first prompt means the agent cannot fake
progress: a turn that does not green one of these tests did not advance
the project.
"""
import pytest


def test_loop_halts_on_empty_plan(loop):
    assert loop.step(plan=[]) == "halt"


def test_loop_consumes_one_tool_call_per_step(loop):
    result = loop.step(plan=["noop_tool"])
    assert result.tool_calls == 1


@pytest.fixture
def loop():
    from todo.agent import AgentLoop
    return AgentLoop()
