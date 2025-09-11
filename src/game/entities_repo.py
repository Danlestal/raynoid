from ast import Dict
from uuid import UUID

from game.components import ComponentType
from game.entity import Entity


class EntitiesRepo:
    def __init__(self):
        self.entities: Dict[UUID, Entity] = {}

    def add_entity(self, entity):
        self.entities[entity.id] = entity

    def remove_entity(self, entity_id):
        if entity_id in self.entities:
            del self.entities[entity_id]


    def get_entity(self, entity_id):
        return self.entities.get(entity_id, None)
    

    def get_all_entities(self):
        return list(self.entities.values())
    

    def get_entities_with_component(self, component_type:ComponentType):
        return [e for e in self.entities.values() if e.has_component(component_type)]
    
    def get_moving_entities(self):
        return [e for e in self.entities.values() if e.is_moving()]
    

    