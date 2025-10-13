from dataclasses import dataclass
from typing import List, Optional

from pyray import Vector2
from game.components import ComponentType
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.event_bus import EventBus, GameEvent
from game.systems.physics.rectangle import Rectangle
from game.systems.system import GameSystem



@dataclass(slots=True)
class CollisionEvent(GameEvent):
    entity1: Entity
    entity2: Entity 
    collision_vector: Vector2
    
class PhysicsSystem(GameSystem):

    def __init__(self,
                 entities_db:EntitiesRepo,
                 event_bus: EventBus):
        self.entities_db:EntitiesRepo = entities_db
        self.event_bus = event_bus
        
    def update(self):
        all_entities: List[Entity] = self.entities_db.get_entities_with_component(component_type=ComponentType.BOUNDING_BOX)
        moving_entities = filter(lambda e: e.has_component(ComponentType.VELOCITY), all_entities)
        processed_pairs = set()
        for moving_entity in moving_entities:
            position: Vector2 = moving_entity.get_component(ComponentType.POSITION).position
            moving_rectangle = Rectangle(
                position=position,
                width=moving_entity.get_component(ComponentType.BOUNDING_BOX).width,
                height=moving_entity.get_component(ComponentType.BOUNDING_BOX).height
            )

            for other_entity in all_entities:
                if moving_entity.id == other_entity.id:
                    continue

                pair = tuple(sorted((moving_entity.id, other_entity.id)))
                if pair in processed_pairs:
                    continue
                processed_pairs.add(pair)

                other_rectangle = Rectangle(
                    position=other_entity.get_component(ComponentType.POSITION).position,
                    width=other_entity.get_component(ComponentType.BOUNDING_BOX).width,
                    height=other_entity.get_component(ComponentType.BOUNDING_BOX).height
                )

                collision_vector: Optional[Vector2] = moving_rectangle.check_collision(other_rectangle)
                if collision_vector is not None:
                    self.event_bus.emit(CollisionEvent(
                        entity1=moving_entity,
                        entity2=other_entity,
                        collision_vector=collision_vector
                    ))


