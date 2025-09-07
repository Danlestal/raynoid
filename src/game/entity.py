from ast import List
from typing import Optional
from game.components import Component, ComponentType


class Entity:
    def __init__(self, id):
        self.id = id
        self.components: List[Optional[Component]] = [None] *(len(ComponentType))

    def add_component(self, component: Component):
        self.components[component.type.value] = component

    def get_component(self, component_type: ComponentType) -> Optional[Component]:
        return self.components[component_type.value]
    
    def remove_component(self, component_type: ComponentType):
        self.components[component_type.value] = None

    def has_component(self, component_type: ComponentType) -> bool:
        return self.components[component_type.value] is not None
    
    def is_moving(self) -> bool:
        return self.has_component(ComponentType.VELOCITY)
                