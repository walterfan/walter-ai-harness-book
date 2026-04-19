# verified: 2026-04-17 · Ch.07 OpenHarness hands-on · adapted from upstream
# "Add a Custom Tool" docs (MIT-licensed OpenHarness by HKUDS, attributed).
"""A minimal custom tool registered into an OpenHarness session.

The upstream pattern is: declare a Pydantic-style input schema, implement
a ``run`` method, and register the tool at startup. The stub below is the
smallest compilable example; in production you would replace ``run`` with
real logic and point ``register_tool`` at your registry of choice.
"""
from dataclasses import dataclass


@dataclass
class WordCountInput:
    text: str


class WordCountTool:
    name = "word_count"
    description = "Return the number of whitespace-separated tokens in `text`."
    input_schema = WordCountInput

    def run(self, inp: WordCountInput) -> int:
        return len(inp.text.split())


def register(registry) -> None:
    """Entry point invoked by OpenHarness at startup.

    See upstream ``docs/tools.md`` for the full registry contract.
    """
    registry.add(WordCountTool())
