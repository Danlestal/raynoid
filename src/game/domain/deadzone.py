from pyray import Vector2
import pyray as rl

from game.domain.ibreakable import IBreakable
from game.domain.twod_entity import TwoD_Entity

class DeadZone(IBreakable, TwoD_Entity):
    def __init__(self, position: Vector2, width: float, height: float):
        self.position = position
        self.width = width
        self.height = height

    def is_breakable(self) -> bool:
        return False

    def draw(self):
        rl.draw_rectangle_v(self.position, Vector2(self.width, self.height), rl.RED)
        
    def get_top_boundary(self):
        return  self.position.y
        
    def get_down_boundary(self):
        return  self.position.y + self.height
    
    def get_left_boundary(self):
        return  self.position.x
    
    def get_right_boundary(self):
        return self.position.x + self.width