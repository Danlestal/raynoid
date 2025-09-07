from unittest.mock import create_autospec
from uuid import uuid4

from pyray import Vector2
from game.components import BoundingRectangle, Position, Velocity
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.event_bus import EventBus
from game.systems.physics.new_physics_system import PhysicsSystem
from game.systems.physics.rectangle import Rectangle


# A boulder is just a rectangle for testing purposes.
def create_entity(x, y, width, height) -> Entity:
    entity = Entity(id = uuid4())
    entity.add_component(Position(position=Vector2(x, y)))
    entity.add_component(BoundingRectangle(width=width, height=height))
    return entity


def create_moving_entity(x, y, width, height) -> Entity:
    entity = create_entity(x, y, width, height)
    entity.add_component(Velocity(vector=(1,1))) # This is not really interesting, the only purpose is to mark the entity as moving.
    return entity


def test_physics_WHEN_no_entities_THEN_nothing_happens():
    # Arrange
    entities_db: EntitiesRepo = create_autospec(EntitiesRepo)
    entities_db.get_entities_with_component.return_value = []
    event_bus = create_autospec(EventBus)

    # Act
    phys_systems = PhysicsSystem(entities_db=entities_db, event_bus=event_bus)
    phys_systems.update()
    
    # Assert
    assert not event_bus.emit.called

def test_physics_WHEN_no_colliding_entities_THEN_nothing_happens():
    # Arrange
    entities_db: EntitiesRepo = create_autospec(EntitiesRepo)
    entities_db.get_entities_with_component.return_value = [
        create_moving_entity(0, 0, 10, 10),
        create_entity(20, 20, 5, 5)
    ]
    event_bus = create_autospec(EventBus)

    # Act
    phys_systems = PhysicsSystem(entities_db=entities_db, event_bus=event_bus)
    phys_systems.update()
    
    # Assert
    assert not event_bus.emit.called

def test_physics_WHEN_colliding_entities_THEN_collision_event_emitted():
    # Arrange
    moving_entity = create_moving_entity(0, 0, 10, 10)
    static_entity = create_entity(5, 5, 10, 10)

    entities_db: EntitiesRepo = create_autospec(EntitiesRepo)
    entities_db.get_entities_with_component.return_value = [
        moving_entity,
        static_entity
    ]
    event_bus = create_autospec(EventBus)

    # Act
    phys_systems = PhysicsSystem(entities_db=entities_db, event_bus=event_bus)
    phys_systems.update()
    
    # Assert
    event_bus.emit.assert_called_once()
    emitted_event = event_bus.emit.call_args[0][0]
    assert emitted_event.entity1.id == moving_entity.id
    assert emitted_event.entity2.id == static_entity.id
    assert emitted_event.collision_vector == Rectangle.VECTOR_CHANGE_HORIZONTAL 