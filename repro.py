from typing import Any

def foo(a: Any) -> None:
    reveal_type(None)
    assert a is None
    reveal_type(None)

