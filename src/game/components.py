from dataclasses import dataclass
from enum import Enum
from typing import Optional
from pyray import Vector2


class ComponentType(Enum):
    POSITION = 0
    VELOCITY = 1
    BOUNDING_BOX = 2
    SPRITE = 3
    COLLISION_RESPONSE = 4
    HEALTH = 5
    


class Component:
    type: ComponentType

@dataclass(slots=True)
class Position(Component):
    type = ComponentType.POSITION
    position: Vector2

@dataclass(slots=True)
class Velocity(Component):
    type = ComponentType.VELOCITY
    vector: Vector2 

@dataclass(slots=True)
class BoundingRectangle(Component):
    type = ComponentType.BOUNDING_BOX
    width: float
    height: float


class CollisionResponseType(Enum):
    BOUNCE = 0
    DESTROY = 1
    DAMAGE = 2
    TRIGGER = 3
    
@dataclass(slots=True)
class CollisionResponse(Component):
    type = ComponentType.COLLISION_RESPONSE
    response_type: CollisionResponseType
    health: int = 1
    is_destructible: bool = True
    on_hit_callback: Optional[callable] = None

@dataclass(slots=True)
class Health(Component):
    current_health: int
    max_health: int
    is_invulnerable: bool = False
