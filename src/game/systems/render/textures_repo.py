from typing import Optional
from pyray import Texture2D, load_texture



class TextureRepo:
    def __init__(self):
        self.textures = {}

    def load_texture(self, name:str, path:str):
        self.textures[name] = load_texture(path)

    def get_texture(self, name) -> Optional[Texture2D]:
        return self.textures.get(name, None)