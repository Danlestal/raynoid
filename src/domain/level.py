from typing import List, Optional, Protocol
import pyray as rl
from domain.I_2d_entity import I2DEntity
from domain.ball import Ball
from domain.deadzone import DeadZone
from domain.player import Player


class Level(Protocol):
    def draw(self):
        pass

    def next_level(self) ->  Optional["Level"]:
        pass
        
        

class GameLevel(Level):
    entities: List[I2DEntity]
    balls: List[Ball]
    player: Player
    lifes: int
    deadzone: DeadZone
    
    def __init__(self):
        self.entities = []
        self.balls = []
        self.player = None
        self.deadzone = None
        self.lifes = 3
    
    def add_entity(self, entity:I2DEntity) -> None:
        self.entities.append(entity)
        if isinstance(entity,Ball):
            self.balls.append(entity)
            return
             
        if isinstance(entity,Player):
            self.player = entity
            return 
        
        if isinstance(entity,DeadZone):
            self.deadzone = entity
            return 
                
    def remove_entity(self, entity:I2DEntity) -> None:
        self.entities.remove(entity)
        if isinstance(entity, Ball):
            self.balls.remove(entity)
        
    def get_entities(self) -> I2DEntity:
        return self.entities
    
    def draw(self):
        for entity in self.get_entities():
            entity.draw() 
        rl.draw_text(f"VIDAS: {self.lifes}", 10, 40, 20, rl.GRAY)
        