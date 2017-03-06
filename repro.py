from typing import Any

def foo(a: Any) -> None:
    assert a.b is None
    reveal_type(None)

