from typing import Protocol

class IBreakable(Protocol):
    def is_breakable(self) -> bool:
        pass