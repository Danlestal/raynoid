from typing import Optional
from pyray import Vector2



class Rectangle:
    
    VECTOR_CHANGE_HORIZONTAL = Vector2(-1, 1)
    VECTOR_CHANGE_VERTICAL = Vector2(1, -1)

    def __init__(self, position:Vector2, width:float, height:float):
        self.position = position
        self.width = width
        self.height = height

    def get_left_boundary(self):
        return self.position.x

    def get_right_boundary(self):
        return self.position.x + self.width

    def get_top_boundary(self):
        return self.position.y

    def get_down_boundary(self):
        return self.position.y + self.height
    
    #Returns the normal collision vector if collision occurs, otherwise returns None
    def check_collision(self, other: "Rectangle" ) -> Optional[Vector2]:
        if (
        self.get_right_boundary() >= other.get_left_boundary() and 
        self.get_left_boundary() <= other.get_right_boundary()):
            if (self.get_down_boundary() >= other.get_top_boundary() and
                self.get_top_boundary() <= other.get_down_boundary()):
                return self._get_collission_vector(other)
        return None
    
    #Returns the normal collision vector
    def _get_collission_vector(self, other: "Rectangle") -> Vector2:
        overlaps = [
            (Rectangle.VECTOR_CHANGE_HORIZONTAL, abs(self.get_left_boundary() - other.get_right_boundary())),   # Collision from right
            (Rectangle.VECTOR_CHANGE_HORIZONTAL, abs(self.get_right_boundary() - other.get_left_boundary())),    # Collision from left
            (Rectangle.VECTOR_CHANGE_VERTICAL, abs(self.get_top_boundary() - other.get_down_boundary())),     # Collision from below
            (Rectangle.VECTOR_CHANGE_VERTICAL, abs(self.get_down_boundary() - other.get_top_boundary())),      # Collision from above
        ]
        return min(overlaps, key=lambda x: x[1])[0]