from pico2d import *

open_canvas()

grass = load_image('grass.png')
character_walk = load_image('character_walk.png')
character_roll = load_image('character_roll.png')
character_attack = load_image('character_attack.png')

x=20
frame=0

def char_walk(x,frame):
    while (x < 800):
        clear_canvas()
        grass.draw(400, 30)

        character_walk.clip_draw(frame * 80, 0, 80, 110, x, 90)
        update_canvas()
        frame = (frame + 1) % 6
        x += 5
        delay(0.01)
        get_events()

def char_roll(x,frame):
    while (x < 800):
        clear_canvas()
        grass.draw(400, 30)

        character_roll.clip_draw(frame * 125, 0, 125, 150, x, 90)
        update_canvas()
        frame = (frame + 1) % 9
        x += 10

        delay(0.03)
        get_events()

def char_attack(x,frame):
    while (x < 800):
        clear_canvas()
        grass.draw(400, 30)

        character_attack.clip_draw(frame * 80, 0, 80, 150, x, 115)
        update_canvas()
        frame = (frame + 1) % 9
        x += 10

        delay(0.05)
        get_events()

char_walk(x, frame)
char_roll(x, frame)
char_attack(x,frame)

close_canvas()

