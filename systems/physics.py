from typing import List, Optional
from domain.ball import Ball
from domain.boulder import Boulder
from domain.deadzone import DeadZone
from domain.player import Player
from pyray import Vector2

class Collision:
    def __init__(self, first_entity, second_entity:Optional[any], collision_vector:Vector2):
        self.first_entity = first_entity
        self.second_entity = second_entity
        self.collision_vector = collision_vector

class BruteForcePhysicsSystem:
    
    def __init__(self,
                 level:List[Boulder],
                 deadzone: DeadZone,
                 game_boundaries:Vector2):
        self.game_boundaries = game_boundaries
        self.deadzone = deadzone
        self.level = level
    
    def _check_game_boundaries(self, ball: Ball) -> Optional[Collision]:
        if ball.position.x - ball.radius <= 0 or ball.position.x + ball.radius >= self.game_boundaries.x:
            return Collision(ball, None, Vector2(-1,1)) #Maybe later we add a wall entity.
        
        if ball.position.y - ball.radius <= 0 or ball.position.y + ball.radius >= self.game_boundaries.y:
            return Collision(ball, None, Vector2(1,-1)) #Maybe later we add a wall entity.

    def _check_player_collision(self,
                                ball: Ball,
                                player: Player) -> Optional[Collision]:
        if (
        (ball.position.x + ball.radius >= player.position.x) and 
        (ball.position.x - ball.radius <= player.position.x + player.width)):
            if (ball.position.y + ball.radius >= player.position.y) and (ball.position.y - ball.radius <= player.position.y + player.height):
                return Collision(ball, player, Vector2(1,-1)) #It will be interesting to switch this to scalar vector.
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
            if (
                (ball.position.x + ball.radius >= boulder.position.x) and 
                (ball.position.x - ball.radius <= boulder.position.x + boulder.width)
            ):
                if (ball.position.y + ball.radius >= boulder.position.y) and (ball.position.y - ball.radius <= boulder.position.y + boulder.height):
                    return Collision(ball, boulder, Vector2(1,-1))
                
        # Check deadzone
        if ball.position.y + ball.radius >= self.deadzone.position.y:
            return Collision(ball, self.deadzone, Vector2(1,-1)) #Maybe later we add a wall entity.
        
        return None