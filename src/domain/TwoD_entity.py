from pyray import Vector2
class TwoD_Entity:
    def get_left_boundary(self):
        raise NotImplementedError()

    def get_right_boundary(self):
        raise NotImplementedError()

    def get_top_boundary(self):
        raise NotImplementedError()

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
        overlaps = {
            Vector2(-1, 1): abs(self.get_left_boundary() - other.get_right_boundary()),   # Collision from right
            Vector2(-1, 1): abs(self.get_right_boundary() - other.get_left_boundary()),   # Collision from left
            Vector2(1, -1): abs(self.get_top_boundary() - other.get_down_boundary()),    # Collision from below
            Vector2(1, -1): abs(self.get_down_boundary() - other.get_top_boundary()),     # Collision from above
        }
        return min(overlaps, key=overlaps.get)