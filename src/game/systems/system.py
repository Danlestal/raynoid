from typing import Protocol


class GameSystem(Protocol):
    def update(self):
        pass
    

class ISystem(Protocol):
    def update(self, level):
        pass
    