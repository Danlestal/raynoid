from typing import List

from domain.I_2d_entity import I2DEntity


class Level:
    entities: List[I2DEntity]
    
    def __init__(self):
        self.entities = []
    
    def add_entity(self, entity:I2DEntity) -> None:
        self.entities.append(entity)
        
    def remove_entity(self, entity:I2DEntity) -> None:
        self.entities.remove(entity)
        
    def get_entities(self) -> I2DEntity:
        return self.entities
    
    def draw(self):
        for entity in self.get_entities():
            entity.draw()