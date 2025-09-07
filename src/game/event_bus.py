from ast import List
from collections.abc import Callable
from dataclasses import dataclass
from typing import Dict

@dataclass
class GameEvent:
    pass


class EventBus:
    def __init__(self):
        self._subscribers: Dict[type, List[Callable]] = {}
    
    def subscribe(self, event_type: type, callback: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)
    
    def unsubscribe(self, event_type: type, callback: Callable):
        if event_type in self._subscribers:
            self._subscribers[event_type].remove(callback)
    
    def emit(self, event: GameEvent):
        event_type = type(event)
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                callback(event)