from typing import Any

def foo(a: Any) -> Any:

    assert a.b is None

    reveal_type(None)

