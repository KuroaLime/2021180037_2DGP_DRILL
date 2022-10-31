from pico2d import *

# 이벤트 정의
RD, LD, RU, LU,OTU,OTD, TIMER = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): OTD,
    (SDL_KEYUP, SDLK_a): OTU
}


# 클래스를 이용해서 상태를 만듦
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir=0 #정지 상태
        self.timer =1000

    @staticmethod
    def exit(self):
        print('EXIT IDLE')


    @staticmethod
    def do(self):
        self.frame = (self.frame+1) % 8
        self.timer -=10
        if self.timer ==0:
            self.add_event(TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self. dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1 ) % 8
        self.x += self.dir
        self.x = clamp(0,self.x, 800)


    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir=0 #정지 상태


    @staticmethod
    def exit(self):
        print('EXIT SLEEP')


    @staticmethod
    def do(self):
        self.frame = (self.frame+1) % 8


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, -3.141592/2,'',self.x, self.y,100,100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, 3.141592/2,'',self.x, self.y,100,100)

class AUTO:
    @staticmethod
    def enter(self, event):
        print('ENTER AUTO')
        if self.face_dir == -1:
            self.dir = -1
        else:
            self.dir = 1
    @staticmethod
    def exit(self):
        print('EXIT AUTO')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

        if self.x >= 800:
            self.dir = -1
        elif self.x <=0:
            self.dir = 1
        self.x += self.dir
        # self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


next_state = {
    AUTO: {RU:RUN, LU:RUN, RD:RUN, LD:RUN, OTD:RUN, OTU:AUTO, TIMER:AUTO},
    SLEEP: {RU:RUN, LU:RUN, RD:RUN, LD:RUN, OTD:AUTO, OTU:RUN, TIMER:SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, OTD:AUTO, OTU:RUN, TIMER:SLEEP},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, OTD:AUTO, OTU:IDLE, TIMER:RUN}
}


class Boy:
    def __init__(self):
        self.x, self.y = 10, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)


    def update(self):
        self.cur_state.do(self)

        if self.event_que:  # 큐에 뭔가 들어 있다면,
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

        #
        # else:
        #

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):  # 소년이 스스로 이벤트를 처리할 수 있게...
        # event 는 키 이벤트... 이 것을 내부 RD등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)  # 변환된 내부 key event를 큐에 추가

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1
