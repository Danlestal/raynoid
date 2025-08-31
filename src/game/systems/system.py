from typing import Protocol

class ISystem(Protocol):
    def update(self, level):
        pass
    