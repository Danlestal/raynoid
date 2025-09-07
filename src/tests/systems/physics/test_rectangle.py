import pytest
from pyray import Vector2
from game.systems.physics.rectangle import Rectangle


def test_overlapping_rectangles_should_collide():
    """Test that overlapping rectangles detect collision"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)  # 0,0 to 10,10
    rect2 = Rectangle(Vector2(5, 5), 10, 10)  # 5,5 to 15,15 (overlaps)
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector is not None
    assert collision_vector == Rectangle.VECTOR_CHANGE_HORIZONTAL


def test_non_overlapping_rectangles_should_not_collide():
    """Test that separated rectangles don't detect collision"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(20, 20), 5, 5)  # No overlap
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector is None


def test_touching_rectangles_should_collide():
    """Test edge case where rectangles just touch"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(10, 0), 5, 5)  # Touches right edge
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector == Rectangle.VECTOR_CHANGE_HORIZONTAL


def test_identical_rectangles_should_collide():
    """Test that identical rectangles collide"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(0, 0), 10, 10)
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector == Rectangle.VECTOR_CHANGE_HORIZONTAL


def test_horizontal_collision_returns_horizontal_vector():
    """Test collision from horizontal direction returns horizontal vector"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(8, 2), 5, 6)  # Overlaps horizontally
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector == Rectangle.VECTOR_CHANGE_HORIZONTAL


def test_vertical_collision_returns_vertical_vector():
    """Test collision from vertical direction returns vertical vector"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(2, 8), 6, 5)  # Overlaps vertically
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector == Rectangle.VECTOR_CHANGE_VERTICAL


def test_collision_is_symmetric():
    """Test that A.check_collision(B) behaves consistently with B.check_collision(A)"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(5, 5), 10, 10)
    
    collision1 = rect1.check_collision(rect2)
    collision2 = rect2.check_collision(rect1)
    
    assert collision1 == collision2 == Rectangle.VECTOR_CHANGE_HORIZONTAL



def test_rectangle_inside_another_should_collide():
    """Test when one rectangle is completely inside another"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(2, 2), 3, 3)  # Inside rect1
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector is not None


def test_no_collision_on_x_axis_only():
    """Test rectangles that align on Y but not X don't collide"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(15, 0), 5, 10)
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector is None


def test_no_collision_on_y_axis_only():
    """Test rectangles that align on X but not Y don't collide"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(0, 15), 10, 5)
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector is None


def test_minimal_overlap_collision():
    """Test minimal overlap (1 pixel) still detects collision"""
    rect1 = Rectangle(Vector2(0, 0), 10, 10)
    rect2 = Rectangle(Vector2(9, 9), 5, 5)  # 1x1 overlap
    
    collision_vector = rect1.check_collision(rect2)
    assert collision_vector is not None


@pytest.mark.parametrize("pos1,size1,pos2,size2,expected", [
    (Vector2(0, 0), (10, 10), Vector2(5, 5), (10, 10), True),   # Overlap
    (Vector2(0, 0), (10, 10), Vector2(20, 20), (5, 5), False), # No overlap
    (Vector2(0, 0), (10, 10), Vector2(10, 0), (5, 5), True),   # Touch
])
def test_collision_parametrized(pos1, size1, pos2, size2, expected):
    """Parametrized test for various collision scenarios"""
    rect1 = Rectangle(pos1, size1[0], size1[1])
    rect2 = Rectangle(pos2, size2[0], size2[1])
    
    collision = rect1.check_collision(rect2)
    assert (collision is not None) == expected