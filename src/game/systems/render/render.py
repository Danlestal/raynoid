from typing import List, Protocol

import pyray as rl
from pyray import Rectangle as RLRectangle
from game.components import ComponentType, Position
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.systems.render.textures_repo import TextureRepo
from game.systems.system import GameSystem


class LowLevelRender(Protocol):
    
    def draw_texture():
        pass

    def draw_rectangle():
        pass

    def draw_circle():
        pass

    

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

            if texture:
                position: Position = entity.get_component(ComponentType.POSITION)
                source_rect = RLRectangle(0, 0, 32, 32)
                dest_rect = RLRectangle(
                    position.position.x + sprite.offset.x,
                    position.position.y + sprite.offset.y,
                    sprite.width,
                    sprite.height
                )
                rl.draw_texture_pro(texture, source_rect, dest_rect, rl.Vector2(0, 0), 0, rl.WHITE)
                # rl.draw_rectangle_lines_ex(dest_rect, 1, rl.RED)


