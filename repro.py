from typing import Any, Optional

def foo(a: Any) -> None:
    reveal_type(a)
    assert a is None
    reveal_type(None)

