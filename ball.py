from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    # fill here
    def get_bb(self): # 사이즈 20x20
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    # 공 - 보이 충돌 처리
    def handle_collision(self, group, other):
        if group == 'Boy:Ball':
            # 스스로 없어지기
            game_world.remove_object(self)
        if group == 'Ball:Zombie':
            game_world.remove_object(self)
            pass
            # game_world.remove_object(self)

    def get_velo(self):
        return self.velocity