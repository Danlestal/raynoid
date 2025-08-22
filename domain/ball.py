
from pyray import Vector2
import pyray as rl

class Ball:
    def __init__(self, initial_position: Vector2, initial_vector: Vector2, radius: float):
        self.position = initial_position
        self.vector = initial_vector
        self.radius = radius
        
    def updatePosition(self):
        self.position.x += self.vector.x
        self.position.y += self.vector.y
        
    def updateVector(self, new_vector: Vector2):
        self.vector = new_vector

    def draw(self):
        rl.draw_circle_v(self.position, self.radius, rl.GREEN)