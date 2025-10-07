
import pyray as rl

from game.entities_repo import EntitiesRepo

from game.systems.render.render import RenderSystem
from game.systems.render.textures_repo import TextureRepo
from raynoid.factories.level import LevelFactory


def main():
    # Initialization
    screen_width = 800
    screen_height = 450


    rl.init_window(screen_width, screen_height, "Raynoid")
    rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second

    entities_repo = EntitiesRepo()



    texture_repo = TextureRepo()
    texture_repo.load_texture("boulder", "./resources/raynoid/red.png")
    texture_repo.load_texture("wall", "./resources/raynoid/brick_wall.png")
    

    factory = LevelFactory(entities_repo)
    factory.load_harcoded_level()
  
    render_system = RenderSystem(entities_repo, texture_repo)
    while not rl.window_should_close():
        # ----------------------------------------------------------------------------------
        # Draw
        # ----------------------------------------------------------------------------------
        rl.begin_drawing()
        rl.clear_background(rl.BLACK)
        render_system.update() 
        rl.end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    rl.close_window() 



if __name__ == '__main__':
    main()
