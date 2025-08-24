from typing import Protocol


class I2DEntity(Protocol):
    def get_left_boundary(self):
        pass

    def get_right_boundary(self):
        pass

    def get_top_boundary(self):
        pass

    def get_down_boundary(self):
        pass
    