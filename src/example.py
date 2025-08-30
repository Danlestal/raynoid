
import pyray as rl
from pyray import Vector2
from typing import List

from domain.ball import Ball
from domain.boulder import Boulder
from domain.deadzone import DeadZone
from domain.level import GameLevel, Level
from domain.player import Player
from systems.physics import BruteForcePhysicsSystem

def configure_level_boulders(level: Level) -> List[Boulder]:
    start_x = 50
    start_y = 50
    width = 60
    height = 20
    padding = 10
    rows = 5
    cols = 10

    for row in range(rows):
        for col in range(cols):
            position = Vector2(start_x + col * (width + padding), start_y + row * (height + padding))
            boulder = Boulder(position=position, width=width, height=height)
            level.add_entity(boulder)

    return level

def main():
    # Initialization
    screen_width = 800
    screen_height = 450
    lifes = 3

    rl.init_window(screen_width, screen_height, "Arkanoid")
    rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second

    
    game_level = GameLevel()
    ball = Ball(initial_position=Vector2(400, 225),
                initial_vector=Vector2(3, -3),
                radius=10)
    game_level.add_entity(ball)
    
    dead_zone = DeadZone(position=Vector2(0, screen_height-5), width=screen_width, height=5)
    game_level.add_entity(dead_zone)
    
    player = Player(position=Vector2(screen_width/2 - 50, screen_height-30), width=80, height=20)
    game_level.add_entity(player)
    
    level: List[Boulder] = configure_level_boulders(game_level)
    physics_system = BruteForcePhysicsSystem(level,
                                             Vector2(screen_width, screen_height))   

    # Main game loop
    while not rl.window_should_close():
        # --------------
        # Read keyboard
        # ----------------------------------------------------------------------------------
        if rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
            player.speed.x += 1.5
        if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
            player.speed.x -= 1.5
        

        # Update game logic
        game_level.update_logic()
        physics_system.update()
        # Draw
        # ----------------------------------------------------------------------------------
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        game_level.draw()
        rl.end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    rl.close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
