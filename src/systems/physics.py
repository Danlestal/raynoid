from typing import Optional
from domain.ball import Ball
from domain.boulder import Boulder
from pyray import Vector2
from domain.deadzone import DeadZone
from domain.level import GameLevel
from domain.player import Player
from pyray import Vector2

from systems.system import ISystem

class Collision:
    def __init__(self,
                 first_entity,
                 second_entity:Optional[any],
                 collision_vector:Vector2):
        self.first_entity = first_entity
        self.second_entity = second_entity
        self.collision_vector = collision_vector

class BruteForcePhysicsSystem(ISystem):
    
    def __init__(self,
                 level:GameLevel,
                 game_boundaries:Vector2):
        self.game_boundaries = game_boundaries
        self.level = level
        
    
    def _check_game_boundaries(self, ball: Ball) -> Optional[Collision]:
        if ball.get_left_boundary() <= 0 or ball.get_right_boundary() >= self.game_boundaries.x:
            return Collision(ball, None, Vector2(-1,1)) #Maybe later we add a wall entity.
        
        if ball.get_top_boundary() <= 0 or ball.get_down_boundary() >= self.game_boundaries.y:
            return Collision(ball, None, Vector2(1,-1)) #Maybe later we add a wall entity.

    def _check_player_collision(self,
                                ball: Ball,
                                player: Player) -> Optional[Collision]:
        if (ball.check_collision(player)):
            return Collision(ball, player, Vector2(1,-1))
        return None


    def update(self):
        collisions = map(lambda ball: self._detect_collision(ball,self.level.player),
                         self.level.balls)
        for collision in collisions:
            if collision:
                ball = collision.first_entity
                ball.on_collision(collision.collision_vector)
                if (collision.second_entity):
                    if (collision.second_entity.is_breakable()):
                        self.level.remove_entity(collision.second_entity)

                    if (isinstance(collision.second_entity, DeadZone)):
                        self.level.lifes -= 1
            
            
    def _detect_collision(self,
                         ball: Ball,
                         player:Player ) -> Optional[Collision]:
        # Check boundaries
        collision_detected = self._check_game_boundaries(ball)
        if collision_detected:
            return collision_detected
        
        # Check player collision
        collision_detected = self._check_player_collision(ball, player)
        if collision_detected:
            return collision_detected

        # Check boulder collision
        for boulder in filter(lambda x: isinstance(x,Boulder), self.level.get_entities()):
            if ball.check_collision(boulder):
                return Collision(ball, boulder, ball.get_collission_vector(boulder))     
                
        if ball.get_down_boundary() >= self.level.deadzone.position.y:
            return Collision(ball, self.level.deadzone, Vector2(1,-1))
        
        return None