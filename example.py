
import pyray as rl
from pyray import Vector2
from typing import List

from domain.ball import Ball
from domain.boulder import Boulder
from domain.deadzone import DeadZone
from domain.player import Player
from systems.physics import BruteForcePhysicsSystem

def configure_level() -> List[Boulder]:
    level: List[Boulder] = []
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
            level.append(boulder)

    return level

def main():
    # Initialization
    screen_width = 800
    screen_height = 450
    lifes = 3

    rl.init_window(screen_width, screen_height, "Arkanoid")
    rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second

    
    ball = Ball(initial_position=Vector2(400, 225),
                initial_vector=Vector2(3, -3),
                radius=10)
    dead_zone = DeadZone(position=Vector2(0, screen_height-5), width=screen_width, height=5)
    player = Player(position=Vector2(screen_width/2 - 50, screen_height-30), width=80, height=20)
    level: List[Boulder] = configure_level()
    physics_system = BruteForcePhysicsSystem(level, Vector2(screen_width, screen_height))   

    # Main game loop
    while not rl.window_should_close():
        
        # Read keyboard
        # ----------------------------------------------------------------------------------
        if rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
            player.speed.x += 1.5
        if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
            player.speed.x -= 1.5
        

        # Update game logic
        ball.update_position()
        player.update_position()
        collision = physics_system.detect_collision(ball, player)
        if collision:
            ball.on_collision(collision.collision_vector)
            if (collision.second_entity and collision.second_entity.is_breakable()):
                level.remove(collision.second_entity)
                physics_system.remove_entity(collision.second_entity)

        # Draw
        # ----------------------------------------------------------------------------------
        rl.begin_drawing()

        rl.clear_background(rl.RAYWHITE)
        ball.draw()
        player.draw()
        dead_zone.draw()
        for boulder in level:
            boulder.draw()
            
        rl.draw_text(f"VIDAS: {lifes}", 10, 40, 20, rl.GRAY)
        rl.draw_text(f"PUNTUACION", 600, 40, 20, rl.GRAY)

        rl.end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    rl.close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
