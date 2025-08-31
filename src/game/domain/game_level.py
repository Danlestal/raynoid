from typing import List
import pyray as rl
from game.domain.boulder import Boulder
from game.domain.level import Level
from game.domain.twod_entity import TwoD_Entity
from game.domain.ball import Ball
from game.domain.deadzone import DeadZone
from game.domain.player import Player
from game.systems.system import ISystem



class GameLevel(Level):
    def __init__(self, systems:List[ISystem] ):
        self.entities: List[TwoD_Entity] = []
        self.balls: List[Ball] = []
        self.player: Player = None
        self.deadzone: DeadZone = None
        self.lifes: int = 3
        self.systems: List[ISystem] = systems
    
    def add_entity(self, entity:TwoD_Entity) -> None:
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
                
    def remove_entity(self, entity:TwoD_Entity) -> None:
        self.entities.remove(entity)
        if isinstance(entity, Ball):
            self.balls.remove(entity)
        
    def get_entities(self) -> TwoD_Entity:
        return self.entities
    
    def draw(self):
        for entity in self.get_entities():
            entity.draw() 
        rl.draw_text(f"VIDAS: {self.lifes}", 10, 40, 20, rl.GRAY)
        
    def get_remaining_boulders(self):
        return len(set(filter(lambda x: isinstance(x,Boulder), self.entities)))
    
    def next_level(self):
        if self.lifes == 0 or self.get_remaining_boulders() == 0:
            return GameScoreLevel()

    def update_systems(self):
        for system in self.systems:
            system.update(self)