from abc import abstractmethod
from typing import Protocol


class IMovingEntity(Protocol):
    @abstractmethod
    def update_position(self):
        pass