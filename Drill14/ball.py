import random
import game_framework
from pico2d import *

import game_world
import server


class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(50, server.background.w - 50)
        self.y = random.randint(50, server.background.h - 50)

    def update(self):
        pass
    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        self.image.clip_draw(0, 0, 21, 21, sx, sy)
    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def handle_collision(self, other, group):
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if group == 'Boy:Ball':
            other.ball_count += 1
            game_world.remove_object(self)

