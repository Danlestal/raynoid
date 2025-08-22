from pyray import Vector2
import pyray as rl

class Boulder:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        
    def draw(self):
        rl.draw_rectangle_v(self.position, Vector2(self.width, self.height), rl.PINK)