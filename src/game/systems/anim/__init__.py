from typing import List
from game.components import AnimatedSprite, ComponentType
from game.entities_repo import EntitiesRepo
from game.entity import Entity
from game.systems.system import GameSystem

class AnimationSystem(GameSystem):
    def __init__(self,
                 entities_db: EntitiesRepo,):
        self.entities_db: EntitiesRepo = entities_db
        self.delta_time = 1 / 60.0

    def update(self):
        animated_entities: List[Entity] = self.entities_db.get_entities_with_component(component_type=ComponentType.SPRITE)
        for entity in animated_entities:

            sprite = entity.get_component(ComponentType.SPRITE)
            if sprite is None or not isinstance(sprite, AnimatedSprite):
                continue
            
            sprite.elapsed_time += self.delta_time
            if sprite.elapsed_time >= sprite.frame_duration:
                sprite.current_frame = (sprite.current_frame + 1) % sprite.total_frames
                sprite.elapsed_time = 0.0