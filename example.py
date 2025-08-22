
import pyray as rl
from pyray import Vector2
from typing import List

from domain.ball import Ball
from domain.boulder import Boulder
from domain.deadzone import DeadZone
from domain.player import Player


def detectCollision(ball: Ball,
                    player:Player,
                    dead_zone: DeadZone,
                    level: List[Boulder],
                    lifes: int, 
                    screen_width: int, 
                    screen_height: int):
    if (ball.position.x + ball.radius >= screen_width) or (ball.position.x - ball.radius <= 0):
        ball.vector.x *= -1
    if (ball.position.y + ball.radius >= screen_height) or (ball.position.y - ball.radius <= 0):
        ball.vector.y *= -1

    if (
        (ball.position.x + ball.radius >= player.position.x) and 
        (ball.position.x - ball.radius <= player.position.x + player.width)):
        if (ball.position.y + ball.radius >= player.position.y) and (ball.position.y - ball.radius <= player.position.y + player.height):
            ball.vector.y *= -1

    if (
        (ball.position.x + ball.radius >= dead_zone.position.x) and
        (ball.position.x - ball.radius <= dead_zone.position.x + dead_zone.width)
    ):
        if (ball.position.y + ball.radius >= dead_zone.position.y) and (ball.position.y - ball.radius <= dead_zone.position.y + dead_zone.height):
            ball.vector.y *= -1
            lifes -= 1
            
    for boulder in level:
        if (
            (ball.position.x + ball.radius >= boulder.position.x) and 
            (ball.position.x - ball.radius <= boulder.position.x + boulder.width)
        ):
            if (ball.position.y + ball.radius >= boulder.position.y) and (ball.position.y - ball.radius <= boulder.position.y + boulder.height):
                ball.vector.y *= -1
                level.remove(boulder)
                break

    return lifes

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

    # Main game loop
    ball = Ball(initial_position=Vector2(400, 225),
                initial_vector=Vector2(3, -3),
                radius=10)
    dead_zone = DeadZone(position=Vector2(0, screen_height-5), width=screen_width, height=5)
    player = Player(position=Vector2(screen_width/2 - 50, screen_height-30), width=80, height=20)
    level: List[Boulder] = configure_level()


    while not rl.window_should_close():
        
        # Read keyboard
        # ----------------------------------------------------------------------------------
        if rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
            player.position.x += 5.0
        if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
            player.position.x -= 5.0
        # if rl.is_key_down(rl.KeyboardKey.KEY_UP):
        #     player.position.y -= 5.0
        # if rl.is_key_down(rl.KeyboardKey.KEY_DOWN):
        #     player.position.y += 5.0

        # Update game logic
        ball.updatePosition()
        lifes = detectCollision(ball,
                                player,
                                dead_zone,
                                level,
                                lifes,
                                screen_width,
                                screen_height)

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
