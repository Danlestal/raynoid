from game.domain.level import GameLevel
from game.systems.system import ISystem


class Logic(ISystem):
            
    def update(self, level:GameLevel):
        for ball in level.balls:
            ball.update_position()
            
        level.player.update_position()
    