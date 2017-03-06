from typing import Any

def foo(a: Any) -> Any:

    assert a.b is None, "message"

    reveal_type(None)

