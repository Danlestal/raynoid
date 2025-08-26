from pyray import Vector2
class I2DEntity:
    def get_left_boundary(self):
        raise NotImplementedError()

    def get_right_boundary(self):
        raise NotImplementedError()

    def get_top_boundary(self):
        raise NotImplementedError()

    def get_down_boundary(self):
        raise NotImplementedError()
    
    def check_collision(self, other: "I2DEntity" ) -> bool:
        if (
        self.get_right_boundary() >= other.get_left_boundary() and 
        self.get_left_boundary() <= other.get_right_boundary()):
            if (self.get_down_boundary() >= other.get_top_boundary() and
                self.get_top_boundary() <= other.get_down_boundary()):
                return True
        return False
    
    
    #Returns the normal collision vector
    def get_collission_vector(self, other: "I2DEntity") -> Vector2:
        surface_distances = {
            Vector2(-1, 1): self.get_left_boundary() - other.get_right_boundary(),
            Vector2(1, 1): other.get_left_boundary() - self.get_right_boundary(),
            Vector2(1, -1): self.get_top_boundary() - other.get_down_boundary(),
            Vector2(1, 1): other.get_top_boundary() - self.get_down_boundary()
        }
        return max(surface_distances, key=surface_distances.get)