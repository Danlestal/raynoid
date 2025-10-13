from typing import List
from game.components import ComponentType, Position, Velocity
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.systems.system import GameSystem

class LogicSystem(GameSystem):
    def __init__(self,
                 entities_db: EntitiesRepo,):
        self.entities_db: EntitiesRepo = entities_db
        self.delta_time = 1 / 60.0

    def update(self):
        moving_entities: List[Entity] = self.entities_db.get_entities_with_component(component_type=ComponentType.VELOCITY)
        for entity in moving_entities:
            pos_component: Position = entity.get_component(ComponentType.POSITION)
            velocity_component: Velocity = entity.get_component(ComponentType.VELOCITY)
            pos_component.position.x += velocity_component.vector.x 
            pos_component.position.y += velocity_component.vector.y