from typing import Protocol

from domain.I_2d_entity import I2DEntity


class ISystem(Protocol):
    def update(self):
        pass
    