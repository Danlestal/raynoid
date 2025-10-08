from game.components import AnimatedSprite, BoundingRectangle, CollisionResponse, CollisionResponseType, FillMethod, Position, Sprite
from game.entity import Entity
from uuid import uuid4
from pyray import Vector2

def build_boulder(x, y, width, height) -> Entity:
    boulder = Entity(uuid4())
    boulder.add_component(Position(Vector2(x, y)))
    boulder.add_component(BoundingRectangle(width, height))
    boulder.add_component(CollisionResponse(CollisionResponseType.DESTROY))
    boulder.add_component(Sprite(texture_id="boulder", fill_method=FillMethod.STRETCH))
    return boulder

def build_barrier(x, y, width, height) -> Entity:
    barrier = Entity(uuid4())
    barrier.add_component(Position(Vector2(x, y)))
    barrier.add_component(BoundingRectangle(width, height))
    barrier.add_component(CollisionResponse(CollisionResponseType.BOUNCE))
    barrier.add_component(Sprite(texture_id="wall", fill_method=FillMethod.TILE, width=width, height=height))
    return barrier

def build_ball(x,y) -> Entity:
    ball = Entity(uuid4())
    ball.add_component(Position(Vector2(x, y)))
    ball.add_component(BoundingRectangle(64, 64))
    ball.add_component(CollisionResponse(CollisionResponseType.BOUNCE))
    ball.add_component(AnimatedSprite(texture_id="ball",
                                      width=128,
                                      height=128,
                                      frame_height=128,
                                      frame_width=128,
                                      total_frames=16))
    return ball