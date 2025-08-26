from pyray import Vector2
import pyray as rl

from domain.ibreakable import IBreakable
from domain.I_2d_entity import I2DEntity

class DeadZone(IBreakable, I2DEntity):
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