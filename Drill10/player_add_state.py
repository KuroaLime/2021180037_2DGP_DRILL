import pico2d

import game_framework
from pico2d import *

import title_state
import play_state
import random
image=None


def enter():
    global image
    image=load_image('add_delete_boy.png')

    pass

def exit():
    global image
    del image

    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_state.player_count=0
                    game_framework.pop_state()
                case pico2d.SDLK_KP_PLUS:
                    play_state.player_count+=1
                    play_state.boy.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_KP_MINUS:
                    if play_state.player_count != 0:
                        play_state.player_count-=1
                        game_framework.pop_state()


