# verified: 2026-04-17 · pytest skeleton · TDD guardian · written BEFORE the prompt
"""Failing-first skeleton for the `todo add` subcommand.

Run with ``pytest -q tests/test_skeleton.py`` — the test must be red before
any prompt is sent to the coding agent. Turning it green is the agent's
job, not the human's.
"""
import pytest


def test_add_appends_one_item(tmp_path, monkeypatch):
    monkeypatch.setenv("TODO_HOME", str(tmp_path))
    from todo.cmds import add  # noqa: WPS433 — import inside test is intentional

    add.run(["buy milk"])
    assert (tmp_path / "todo.json").read_text().count("buy milk") == 1


def test_add_rejects_empty_title():
    from todo.cmds import add

    with pytest.raises(SystemExit):
        add.run([""])
