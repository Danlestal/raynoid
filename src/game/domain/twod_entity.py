from pyray import Vector2
from abc import ABC, abstractmethod

class TwoD_Entity(ABC):
    
    VECTOR_CHANGE_HORIZONTAL = Vector2(-1, 1)
    VECTOR_CHANGE_VERTICAL = Vector2(1, -1)

    @abstractmethod
    def get_left_boundary(self):
        raise NotImplementedError()

    @abstractmethod
    def get_right_boundary(self):
        raise NotImplementedError()

    @abstractmethod
    def get_top_boundary(self):
        raise NotImplementedError()

    @abstractmethod
    def get_down_boundary(self):
        raise NotImplementedError()
    
    def check_collision(self, other: "TwoD_Entity" ) -> bool:
        if (
        self.get_right_boundary() >= other.get_left_boundary() and 
        self.get_left_boundary() <= other.get_right_boundary()):
            if (self.get_down_boundary() >= other.get_top_boundary() and
                self.get_top_boundary() <= other.get_down_boundary()):
                return True
        return False
    
    #Returns the normal collision vector
    def get_collission_vector(self, other: "TwoD_Entity") -> Vector2:
        overlaps = [
            (TwoD_Entity.VECTOR_CHANGE_HORIZONTAL, abs(self.get_left_boundary() - other.get_right_boundary())),   # Collision from right
            (TwoD_Entity.VECTOR_CHANGE_HORIZONTAL, abs(self.get_right_boundary() - other.get_left_boundary())),    # Collision from left
            (TwoD_Entity.VECTOR_CHANGE_VERTICAL, abs(self.get_top_boundary() - other.get_down_boundary())),     # Collision from below
            (TwoD_Entity.VECTOR_CHANGE_VERTICAL, abs(self.get_down_boundary() - other.get_top_boundary())),      # Collision from above
        ]
        return min(overlaps, key=lambda x: x[1])[0]