
import pyray as rl

from game.entities_repo import EntitiesRepo

from game.event_bus import EventBus
from game.systems.anim import AnimationSystem
from game.systems.collision_response import CollisionResponseSystem
from game.systems.logic import LogicSystem
from game.systems.physics.new_physics_system import CollisionEvent, PhysicsSystem
from game.systems.render.render import RenderSystem
from game.systems.render.textures_repo import TextureRepo
from raynoid.factories.entities import build_ball
from raynoid.factories.level import LevelFactory


def main():
    # Initialization
    screen_width = 800
    screen_height = 450


    rl.init_window(screen_width, screen_height, "Bounce Sandbox")
    rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second

    texture_repo = TextureRepo()
    texture_repo.load_texture("ball", "../resources/raynoid/ball.png")
    texture_repo.load_texture("wall", "../resources/raynoid/brick_wall.png")


    entities_repo = EntitiesRepo()
    factory = LevelFactory(entities_repo)
    factory.add_barriers()
    entities_repo.add_entity(build_ball(420,220, frame_duration=0.07))
    entities_repo.add_entity(build_ball(320,120, frame_duration=0.07))
    entities_repo.add_entity(build_ball(120,220, frame_duration=0.07))

      
    animation_system = AnimationSystem(entities_repo)
    render_system = RenderSystem(entities_repo, texture_repo)
    logic_system = LogicSystem(entities_repo)
    collision_response_system = CollisionResponseSystem(entities_repo)
    event_bus = EventBus()
    event_bus.subscribe(CollisionEvent, collision_response_system.handle_collision_response)
    physics_system = PhysicsSystem(entities_repo, event_bus)
    
    while not rl.window_should_close():
        # ----------------------------------------------------------------------------------
        # Draw
        # ----------------------------------------------------------------------------------
        rl.begin_drawing()
        rl.clear_background(rl.WHITE)
        render_system.update()
        animation_system.update()
        logic_system.update()
        physics_system.update()
        rl.end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    rl.close_window() 



if __name__ == '__main__':
    main()
