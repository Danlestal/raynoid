from unittest.mock import create_autospec, patch
from game.components import ComponentType
from game.entities_repo import EntitiesRepo
from game.systems.render.render import RenderSystem
from game.systems.render.textures_repo import TextureRepo
from raynoid.factories.entities.boulder import build_boulder

@patch("game.systems.render.render.rl.draw_texture_pro")
def test_render_system_WHEN_there_are_no_entities_THEN_nothing_is_drawn(mock_draw_texture_pro):

    entities_db = create_autospec(EntitiesRepo)
    entities_db.get_entities_with_component.return_value = []
    texture_repo = create_autospec(TextureRepo)
    render_system = RenderSystem(entities_db=entities_db,
                                 texture_repo=texture_repo)


    render_system.update()
    assert not mock_draw_texture_pro.called


@patch("game.systems.render.render.rl.draw_texture_pro")
def test_render_system_WHEN_there_are_entities_with_the_required_components_THEN_we_draw(mock_draw_texture_pro):

    entities_db = create_autospec(EntitiesRepo)
    entities_db.get_entities_with_component.return_value = [build_boulder(0,0,32,32)] #An entity with a sprite.
    texture_repo = create_autospec(TextureRepo)
    render_system = RenderSystem(entities_db=entities_db,
                                 texture_repo=texture_repo)


    render_system.update()
    assert mock_draw_texture_pro.called