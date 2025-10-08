from typing import List, Protocol

import pyray as rl
from pyray import Rectangle as RLRectangle
from game.components import ComponentType, FillMethod, Position
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.systems.render.textures_repo import TextureFrame, TextureRepo
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
            texture_frame: TextureFrame = self.texture_repo.get_texture(sprite)

            if texture_frame:
                position: Position = entity.get_component(ComponentType.POSITION)
                dest_rect = RLRectangle(
                    position.position.x + sprite.offset.x,
                    position.position.y + sprite.offset.y,
                    sprite.width,
                    sprite.height
                )
               
                if sprite.fill_method == FillMethod.TILE:
                    self._tile_texture(texture_frame.texture, dest_rect)
                else:
                    rl.draw_texture_pro(texture_frame.texture,
                                        texture_frame.source_rect,
                                        dest_rect,
                                        rl.Vector2(0, 0),
                                        0,
                                        rl.WHITE)

    def _tile_texture(self, texture, dest_rect):
        tile_w, tile_h = texture.width, texture.height
        x0, y0 = int(dest_rect.x), int(dest_rect.y)
        x1, y1 = int(dest_rect.x + dest_rect.width), int(dest_rect.y + dest_rect.height)
        for x in range(x0, x1, tile_w):
            for y in range(y0, y1, tile_h):
                draw_w = min(tile_w, x1 - x)
                draw_h = min(tile_h, y1 - y)
                src_rect = RLRectangle(0, 0, draw_w, draw_h)
                dst_pos = rl.Vector2(x, y)
                rl.draw_texture_rec(texture, src_rect, dst_pos, rl.WHITE)


