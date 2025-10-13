from game.entities_repo import EntitiesRepo
from raynoid.factories.entities import build_barrier, build_boulder


class LevelFactory:
    def __init__(self, entities_repo:EntitiesRepo):
        self.entities_repo = entities_repo
        pass


    def add_barriers(self):
        left_barrier = build_barrier(0, 0, 32, 450)
        right_barrier = build_barrier(800-32, 0, 32, 450)
        top_barrier = build_barrier(0, 0, 800, 32)
        bottom_barrier = build_barrier(0, 450-32, 800, 32)
        self.entities_repo.add_entity(entity=left_barrier)
        self.entities_repo.add_entity(entity=right_barrier)
        self.entities_repo.add_entity(entity=top_barrier)
        self.entities_repo.add_entity(entity=bottom_barrier) 

    def load_harcoded_level(self):
        self.add_barriers()
        columns = 20
        rows = 10

        x_start = 100
        y_start = 65

        for i in range(rows):
            y_step = (i * 20) + y_start
            for j in range(columns):
                x_step = (j*30) + x_start
                boulder = build_boulder(x_step,y_step,32,32)
                self.entities_repo.add_entity(boulder)
