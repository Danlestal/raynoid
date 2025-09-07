from dataclasses import dataclass
from enum import Enum
from pyray import Vector2


class ComponentType(Enum):
    POSITION = 0
    VELOCITY = 1
    BOUNDING_BOX = 2
    SPRITE = 3
    


class Component:
    type: ComponentType

@dataclass(slots=True)
class Position(Component):
    position: Vector2

@dataclass(slots=True)
class BoundingRectangle(Component):
    width: float
    height: float
