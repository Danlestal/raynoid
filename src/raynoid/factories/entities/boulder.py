from game.components import BoundingRectangle, CollisionResponse, CollisionResponseType, Position
from game.entity import Entity
from uuid import uuid4
from pyray import Vector2

def build_boulder(x, y, width, height) -> Entity:
    boulder = Entity(uuid4())
    boulder.add_component(Position(Vector2(x, y)))
    boulder.add_component(BoundingRectangle(width, height))
    boulder.add_component(CollisionResponse(CollisionResponseType.DESTROY))
    return boulder

   