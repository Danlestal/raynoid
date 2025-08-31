import pyray as rl
from pyray import Vector2

from domain.ibreakable import IBreakable
from domain.TwoD_entity import TwoD_Entity
from domain.moving_entity import IMovingEntity

class Player(IBreakable, TwoD_Entity, IMovingEntity):
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        self.speed = Vector2(0,0)

    def update_position(self):
        self.position.x += self.speed.x
        self.position.y += self.speed.y
        self._update_speed_with_friction()

    def _update_speed_with_friction(self):
        if self.speed.x > 0:
            self.speed.x -= 0.5
        if self.speed.x < 0:
            self.speed.x += 0.5

    def draw(self):
        rl.draw_rectangle_v(self.position, Vector2(self.width, self.height), rl.BLUE)
        
    def is_breakable(self) -> bool:
        return False
    
    def get_top_boundary(self):
        return  self.position.y
        
    def get_down_boundary(self):
        return  self.position.y + self.height
    
    def get_left_boundary(self):
        return  self.position.x
    
    def get_right_boundary(self):
        return self.position.x + self.width