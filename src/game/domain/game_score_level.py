
from game.domain.level import Level
import pyray as rl

class GameScoreLevel(Level):
    def draw(self):
         rl.draw_text(f"GAME OVER",  10, 40, 20, rl.BLACK)
    
    def next_level(self):
        return None
    
    def update_systems(self):
        pass
        
