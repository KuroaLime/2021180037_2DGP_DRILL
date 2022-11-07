from pico2d import *

import game_framework
import game_world
from ball import Ball

PIXEL_PER_METER = (10.0/0.3)
BIRD_WEIGHT = 2
RUN_SPEED_KMPH = 17.0/2
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACITON = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACITON
FRAMES_PER_ACTION1 = 5
FRAMES_PER_ACTION2 = 5
FRAMES_PER_ACTION3 = 4

#1 : 이벤트 정의
SPACE, TIMER= range(2)
event_name = ['SPACE','TIMER']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
}


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        pass


    @staticmethod
    def draw(self):
        pass
class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if self.face_dir == 1:
            self.dir += 1
        elif self.face_dir == -1:
            self.dir -= 1
        else:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        if self.frame_turn == 0:
            self.frame = (self.frame + FRAMES_PER_ACTION1 * ACTION_PER_TIME * game_framework.frame_time) % 5
        elif self.frame_turn == 1:
            self.frame = (self.frame + FRAMES_PER_ACTION2 * ACTION_PER_TIME * game_framework.frame_time) % 5
        elif self.frame_turn == 2:
            self.frame = (self.frame + FRAMES_PER_ACTION3 * ACTION_PER_TIME * game_framework.frame_time) % 5

        if self.frame <= 0.04:
            if self.frame_turn < 2:
                self.frame_turn += 1
            else:
                self.frame_turn = 0
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x >=1600:
            self.dir = -1
        elif self.x <=0:
            self.dir = 1
        self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.dir == -1:
            if self.frame_turn == 0:
                self.image.clip_composite_draw(int(self.frame)*183, 336, 183, 168,
                                          0, 'h', self.x, self.y, 100,100)
            elif self.frame_turn == 1:
                self.image.clip_composite_draw(int(self.frame) * 183, 168, 183, 168,
                                               0, 'h', self.x, self.y, 100, 100)
            else:
                self.image.clip_composite_draw(int(self.frame) * 183, 0, 183, 168,
                                               0, 'h', self.x, self.y, 100, 100)
        elif self.dir == 1:
            if self.frame_turn == 0:
                self.image.clip_composite_draw(int(self.frame) * 183, 336, 183, 168,
                                               0, '', self.x, self.y, 100, 100)
            elif self.frame_turn == 1:
                self.image.clip_composite_draw(int(self.frame) * 183, 168, 183, 168,
                                               0, '', self.x, self.y, 100, 100)
            else:
                self.image.clip_composite_draw(int(self.frame) * 183, 0, 183, 168,
                                               0, '', self.x, self.y, 100, 100)

#3. 상태 변환 구현

next_state = {
    IDLE:  {SPACE: RUN},
    RUN:   {SPACE: IDLE}
}




class Bird:
    # image =None
    def __init__(self, x,y):
        self.frame_turn=0
        self.x, self.y = x, y
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        # if Bird.image == None:
        self.image = load_image('bird_animation.png')
        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.font = load_font('ENCR10B.TTF',16)

        key_event = key_event_table[(SDL_KEYDOWN, SDLK_SPACE)]
        self.add_event(key_event)
    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x -60, self.y +50, f'(Time: {get_time():.2f}', (255,255,0))
    def add_event(self, event):
        self.event_que.insert(0, event)

    # def handle_event(self, event):
    #     key_event = key_event_table[(SDL_KEYDOWN, SDLK_SPACE)]
    #     self.add_event(key_event)

    # def fire_ball(self):
    #     print('FIRE BALL')
    #     ball = Ball(self.x, self.y, self.face_dir*2)
    #     game_world.add_object(ball, 1)
