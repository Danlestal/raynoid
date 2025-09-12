
import pyray as rl

from game.entities_repo import EntitiesRepo

from game.systems.render.render import RenderSystem
from game.systems.render.textures_repo import TextureRepo
from raynoid.factories.entities.boulder import build_barrier, build_boulder

def main():
    # Initialization
    screen_width = 800
    screen_height = 450


    rl.init_window(screen_width, screen_height, "Raynoid")
    rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second

    entities_repo = EntitiesRepo()
    boulder = build_boulder(100, 100, 32, 20)
    left_barrier = build_barrier(0, 0, 32, 450)
    right_barrier = build_barrier(800-32, 0, 32, 450)
    top_barrier = build_barrier(0, 0, 800, 32)
    bottom_barrier = build_barrier(0, 450-32, 800, 32)
    entities_repo.add_entity(entity=left_barrier)
    entities_repo.add_entity(entity=right_barrier)
    entities_repo.add_entity(entity=top_barrier)
    entities_repo.add_entity(entity=bottom_barrier)
    entities_repo.add_entity(entity=boulder)

    texture_repo = TextureRepo()
    texture_repo.load_texture("boulder", "../resources/raynoid/red.png")
    render_system = RenderSystem(entities_repo, texture_repo)
    # Main game loop
    while not rl.window_should_close():
        # ----------------------------------------------------------------------------------
        # Draw
        # ----------------------------------------------------------------------------------
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        render_system.update() 
        rl.end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    rl.close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
