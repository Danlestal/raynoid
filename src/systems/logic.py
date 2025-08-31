from domain.level import GameLevel
from systems.system import ISystem


class Logic(ISystem):
    
    def __init__(self, level:GameLevel):
        self.level = level
        
        
    def update(self):
        for ball in self.level.balls:
            ball.update_position()
            
        self.level.player.update_position()
    