
import pyray as rl

from game.entities_repo import EntitiesRepo

from game.systems.anim import AnimationSystem
from game.systems.render.render import RenderSystem
from game.systems.render.textures_repo import TextureRepo
from raynoid.factories.entities import build_ball
from raynoid.factories.level import LevelFactory


def main():
    # Initialization
    screen_width = 800
    screen_height = 450


    rl.init_window(screen_width, screen_height, "Animation Sandbox")
    rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second

    entities_repo = EntitiesRepo()

    texture_repo = TextureRepo()
    texture_repo.load_texture("ball", "../resources/raynoid/ball.png")
    entities_repo.add_entity(build_ball(320,120))
    entities_repo.add_entity(build_ball(420,220, frame_duration=0.1))
    entities_repo.add_entity(build_ball(220,20, frame_duration=0.05))
      
    animation_system = AnimationSystem(entities_repo)
    render_system = RenderSystem(entities_repo, texture_repo)
    while not rl.window_should_close():
        # ----------------------------------------------------------------------------------
        # Draw
        # ----------------------------------------------------------------------------------
        rl.begin_drawing()
        rl.clear_background(rl.WHITE)
        render_system.update()
        animation_system.update()
        rl.end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    rl.close_window() 



if __name__ == '__main__':
    main()
