from game.components import CollisionResponse, CollisionResponseType, ComponentType
from game.entity import Entity
from game.systems.physics.new_physics_system import CollisionEvent
from game.systems.system import GameSystem


class CollisionResponseSystem(GameSystem):
    def __init__(self, entities_db, physics_system):
        self.entities_db = entities_db
        self.physics_system = physics_system

    def update(self):
        for collision_event in self.physics_system.collision_events:
            self._handle_collision_response(collision_event)
        self.physics_system.collision_events.clear()

    def _handle_collision_response(self, collision_event: CollisionEvent):
        entity1 = collision_event.entity1
        entity2 = collision_event.entity2

        # Handle entity1 response
        if entity1.has_component(ComponentType.COLLISION_RESPONSE):
            response = entity1.get_component(ComponentType.COLLISION_RESPONSE)
            self._apply_response(entity1, entity2, response)

        # Handle entity2 response
        if entity2.has_component(ComponentType.COLLISION_RESPONSE):
            response = entity2.get_component(ComponentType.COLLISION_RESPONSE)
            self._apply_response(entity2, entity1, response)

    def _apply_response(self, entity: Entity, other_entity: Entity, response: CollisionResponse):
        if response.response_type == CollisionResponseType.DESTROY:
            if response.is_destructible:
                self.entities_db.remove_entity(entity)
        
        elif response.response_type == CollisionResponseType.DAMAGE:
            if other_entity.has_component(ComponentType.HEALTH):
                health = other_entity.get_component(ComponentType.HEALTH)
                health.current_health -= 1
                if health.current_health <= 0:
                    self.entities_db.remove_entity(other_entity)
        
        elif response.response_type == CollisionResponseType.TRIGGER:
            if response.on_hit_callback:
                response.on_hit_callback(entity, other_entity)