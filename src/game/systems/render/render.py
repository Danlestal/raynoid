from typing import List

import pyray as rl
from pyray import Rectangle as RLRectangle
from game.components import ComponentType, Position
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.systems.render.textures_repo import TextureRepo
from game.systems.system import GameSystem


class RenderSystem(GameSystem):

    def __init__(self,
                 entities_db:EntitiesRepo,
                 texture_repo: TextureRepo):
        self.entities_db:EntitiesRepo = entities_db
        self.texture_repo = texture_repo


    def update(self):
        entities:List[Entity] = self.entities_db.get_entities_with_component(component_type=ComponentType.SPRITE)
        for entity in entities:
            sprite = entity.get_component(ComponentType.SPRITE)
            texture = self.texture_repo.get_texture(sprite.texture_id)

            bounding_box = entity.get_component(ComponentType.BOUNDING_BOX)
            

            if texture:
                position: Position = entity.get_component(ComponentType.POSITION)
                bounding_box = entity.get_component(ComponentType.BOUNDING_BOX)
                source_rect = RLRectangle(0, 0, 32, 32)
                dest_rect = RLRectangle(
                    position.position.x,
                    position.position.y,
                    bounding_box.width,
                    bounding_box.height
                )
                rl.draw_texture_pro(texture, source_rect, dest_rect, rl.Vector2(0, 0), 0, rl.WHITE)


