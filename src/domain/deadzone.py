from pyray import Vector2
import pyray as rl

from domain.ibreakable import IBreakable

class DeadZone(IBreakable):
    def __init__(self, position: Vector2, width: float, height: float):
        self.position = position
        self.width = width
        self.height = height

    def is_breakable(self) -> bool:
        return False

    def draw(self):
        rl.draw_rectangle_v(self.position, Vector2(self.width, self.height), rl.RED)