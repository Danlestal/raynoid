from typing import List

import pyray as rl
from game.components import BoundingRectangle, ComponentType, Position
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.systems.system import GameSystem


class RenderSystem(GameSystem):

    def __init__(self,
                 entities_db:EntitiesRepo):
        self.entities_db:EntitiesRepo = entities_db


    def update(self):
        entities:List[Entity] = self.entities_db.get_entities_with_component(component_type=ComponentType.SPRITE)
        for entity in entities:
            # sprite = entity.get_component(ComponentType.SPRITE)
            # later on this would be a proper sprite render
            component:Position = entity.get_component(ComponentType.POSITION)
            box:BoundingRectangle = entity.get_component(ComponentType.BOUNDING_BOX)
            rl.draw_rectangle_v(component.position, rl.Vector2(box.width, box.height), rl.PINK)

    