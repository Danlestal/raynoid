from typing import Optional, Protocol


class Level(Protocol):
    def draw(self):
        pass

    def next_level(self) ->  Optional["Level"]:
        pass
        
    def update_systems(self):
        pass
    
        for system in self.systems:
            system.update(self)