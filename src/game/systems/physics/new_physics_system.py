from game.components import ComponentType
from game.entities_repo import EntitiesRepo
from game.systems.system import GameSystem

class PhysicsSystem(GameSystem):


    


    def __init__(self, entities_db):
        self.entities_db:EntitiesRepo = entities_db

    def update(self):
        # We assume here that every entity has a position.
        self.entities_db.get_entities_with_component(component_type=ComponentType.BOUNDING_BOX)
        moving_entities = self.entities_db.get_moving_entities()
        for entity in moving_entities:

