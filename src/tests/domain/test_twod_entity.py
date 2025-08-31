from pyray import Vector2
from src.game.domain.twod_entity import TwoD_Entity

class TestEntity(TwoD_Entity):
    def __init__(self, left_boundary, right_boundary, top_boundary, down_boundary):
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.top_boundary = top_boundary
        self.down_boundary = down_boundary
            
    def get_left_boundary(self):
        return self.left_boundary

    def get_right_boundary(self):
        return self.right_boundary

    def get_top_boundary(self):
        return self.top_boundary
    
    def get_down_boundary(self):
        return self.down_boundary
    

def test_no_collision():
    first_entity = TestEntity(2,4,2,4)
    second_entity = TestEntity(6,8,6,8)
    
    assert not first_entity.check_collision(second_entity)
    assert not second_entity.check_collision(first_entity)
    

def test_twod_entity_horizontal_collision():
    first_entity = TestEntity(2,4,2,4)
    second_entity = TestEntity(0,2,2,4)
    
    assert first_entity.check_collision(second_entity)
    assert second_entity.check_collision(first_entity)
    
    collision_vector = first_entity.get_collission_vector(second_entity)
    assert collision_vector == TwoD_Entity.VECTOR_CHANGE_HORIZONTAL
    
    second_collision_vector = second_entity.get_collission_vector(first_entity)
    assert second_collision_vector == TwoD_Entity.VECTOR_CHANGE_HORIZONTAL
    
    
def test_twod_entity_vertical_collision():
    first_entity = TestEntity(0,2,2,4)
    second_entity = TestEntity(0,2,4,6)
    
    assert first_entity.check_collision(second_entity)
    assert second_entity.check_collision(first_entity)
    
    collision_vector = first_entity.get_collission_vector(second_entity)
    assert collision_vector == TwoD_Entity.VECTOR_CHANGE_VERTICAL
    
    second_collision_vector = second_entity.get_collission_vector(first_entity)
    assert second_collision_vector == TwoD_Entity.VECTOR_CHANGE_VERTICAL