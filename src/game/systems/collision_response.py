from pyray import Vector2
from game.components import CollisionResponse, CollisionResponseType, ComponentType
from game.entity import Entity
from game.systems.physics.new_physics_system import CollisionEvent


class CollisionResponseSystem:
    def __init__(self, entities_db):
        self.entities_db = entities_db

    def handle_collision_response(self, collision_event: CollisionEvent):
        entity1 = collision_event.entity1
        entity2 = collision_event.entity2

        # Handle entity1 response
        if entity1.has_component(ComponentType.COLLISION_RESPONSE):
            response = entity1.get_component(ComponentType.COLLISION_RESPONSE)
            self._apply_response(entity1, collision_event.collision_vector, response)

        # Handle entity2 response
        if entity2.has_component(ComponentType.COLLISION_RESPONSE):
            response = entity2.get_component(ComponentType.COLLISION_RESPONSE)
            self._apply_response(entity2, collision_event.collision_vector, response)

    def _apply_response(self, entity: Entity, collision_vector: Vector2, response: CollisionResponse):
        if response.response_type == CollisionResponseType.DESTROY:
            if response.is_destructible:
                self.entities_db.remove_entity(entity)
        
        elif response.response_type == CollisionResponseType.DAMAGE:
            if entity.has_component(ComponentType.HEALTH):
                health = entity.get_component(ComponentType.HEALTH)
                health.current_health -= 1
                if health.current_health <= 0:
                    self.entities_db.remove_entity(entity)
        

        elif response.response_type == CollisionResponseType.BOUNCE:
            if entity.has_component(ComponentType.VELOCITY):
                velocity = entity.get_component(ComponentType.VELOCITY)
                velocity.vector.x *= collision_vector.x
                velocity.vector.y *= collision_vector.y