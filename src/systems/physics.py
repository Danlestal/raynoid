from typing import List, Optional
from domain.ball import Ball
from domain.boulder import Boulder
from pyray import Vector2
from domain.player import Player
from pyray import Vector2

from domain.I_2d_entity import I2DEntity

class Collision:
    def __init__(self,
                 first_entity,
                 second_entity:Optional[any],
                 collision_vector:Vector2):
        self.first_entity = first_entity
        self.second_entity = second_entity
        self.collision_vector = collision_vector

class BruteForcePhysicsSystem:
    
    def __init__(self,
                 level:List[I2DEntity],
                 deadzone: I2DEntity,
                 game_boundaries:Vector2):
        self.game_boundaries = game_boundaries
        self.deadzone = deadzone
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

    def remove_entity(self, entity):
        if isinstance(entity, Boulder):
            if entity in self.level:
                self.level.remove(entity)

    def detect_collision(self,
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
        for boulder in self.level:
            if ball.check_collision(boulder):
                return Collision(ball, boulder, ball.get_collission_vector(boulder))     
                
        # Check deadzone
        if ball.get_down_boundary() >= self.deadzone.position.y:
            return Collision(ball, self.deadzone, Vector2(1,-1))
        
        return None