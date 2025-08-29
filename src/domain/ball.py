
from pyray import Vector2
import pyray as rl

from domain.ibreakable import IBreakable
from domain.I_2d_entity import I2DEntity
from domain.moving_entity import IMovingEntity



class Ball(IBreakable, I2DEntity, IMovingEntity):
    def __init__(self, initial_position: Vector2, initial_vector: Vector2, radius: float):
        self.position = initial_position
        self.vector = initial_vector
        self.radius = radius
        
    def update_position(self):
        self.position.x += self.vector.x
        self.position.y += self.vector.y
        
    def on_collision(self, collision_vector: Vector2):
        self.vector.x *= collision_vector.x
        self.vector.y *= collision_vector.y

    def draw(self):
        rl.draw_circle_v(self.position, self.radius, rl.GREEN)
        
    def is_breakable(self) -> bool:
        return False
    
    def get_down_boundary(self):
        return  self.position.y + self.radius
    
    def get_top_boundary(self):
        return  self.position.y - self.radius
    
    def get_left_boundary(self):
        return  self.position.x - self.radius
    
    def get_right_boundary(self):
        return  self.position.x + self.radius

