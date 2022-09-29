from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global dir_lr, dir_ud
    global last_dir
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type ==SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_lr += 1
                last_dir = 1
            elif event.key == SDLK_LEFT:
                dir_lr -= 1
                last_dir = -1
            elif event.key == SDLK_UP:
                dir_ud +=1
            elif event.key == SDLK_DOWN:
                dir_ud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
               dir_lr-=1
            elif event.key == SDLK_LEFT:
                dir_lr+=1
            elif event.key == SDLK_UP:
                dir_ud-=1
            elif event.key == SDLK_DOWN:
                dir_ud+=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def Animation_change():

    if dir_lr > 0 and dir_ud == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir_lr < 0 and dir_ud == 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif dir_lr == 0 and dir_ud == 0:
        if last_dir == 1:
            character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    elif dir_ud >0:
        if last_dir == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif dir_ud <0:
        if last_dir == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

def stop_search():
    global x,y
    if x<=0:
        x+=5
    elif x>=KPU_WIDTH:
        x-=5
    elif y<=0:
        y+=5
    elif y>=KPU_HEIGHT:
        y-=5

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
dir_ud=0
dir_lr=0
x=800/2
y=800/2

last_dir=0

frame = 0
hide_cursor()


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    Animation_change()
    update_canvas()
    frame = (frame + 1) % 8

    x+=dir_lr*5
    y+=dir_ud*5
    handle_events()
    delay(0.01)
    stop_search()

close_canvas()




