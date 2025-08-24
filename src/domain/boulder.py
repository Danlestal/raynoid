from pyray import Vector2
import pyray as rl
from domain.ibreakable import IBreakable

class Boulder(IBreakable):
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        
    def draw(self):
        rl.draw_rectangle_v(self.position, Vector2(self.width, self.height), rl.PINK)
        
    def is_breakable(self) -> bool:
        return True