from dataclasses import dataclass
from typing import Optional
from pyray import Texture2D, load_texture

from game.components import AnimatedSprite, Sprite
from pyray import Rectangle as RLRectangle

@dataclass
class TextureFrame:
    texture: Texture2D
    source_rect: RLRectangle

class TextureRepo:
    def __init__(self):
        self.textures = {}

    def load_texture(self, name:str, path:str):
        self.textures[name] = load_texture(path)

    def _calculate_source_rectangle(self, sprite:Sprite) -> RLRectangle:
        if isinstance(sprite, AnimatedSprite):
            return RLRectangle(sprite.frame_width * sprite.current_frame,
                               0,
                               sprite.frame_width,
                               sprite.frame_height)

        return RLRectangle(0,
                           0,
                           sprite.width,
                           sprite.height)

    def get_texture(self, sprite: Sprite) -> Optional[TextureFrame]:
        texture = self.textures.get(sprite.texture_id, None)
        if not texture:
            return None
        
        rectangle = self._calculate_source_rectangle(sprite)

        return TextureFrame(texture=texture, source_rect=rectangle)
        