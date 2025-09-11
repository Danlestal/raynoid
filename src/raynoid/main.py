
import pyray as rl

from game.entities_repo import EntitiesRepo
from game.systems.render import RenderSystem
from raynoid.factories.entities.boulder import build_boulder

def main():
    # Initialization
    screen_width = 800
    screen_height = 450


    rl.init_window(screen_width, screen_height, "LOL")
    rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second

    entities_repo = EntitiesRepo()
    boulder = build_boulder(100, 100, 50, 50)
    entities_repo.add_entity(entity=boulder)
    render_system = RenderSystem(entities_repo)
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
