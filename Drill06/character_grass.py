from pico2d import *
import math

open_canvas(800,800)

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
radian=180
moving_count=0

def foward_person(x,y):
    clear_canvas_now()
    character.draw_now(x,y)
    
while(True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)

    if moving_count==0:
        if x<800 and y==90:
            x=x+2
        elif x>=800 and y<400:
            y=y+2
        elif x> 0 and y>=400:
            x=x-2
        elif x<=0 and y>0:
            y=y-2
            if( y==90):
                moving_count+=1
            
        delay(0.001)
    if moving_count == 1:
        if(radian<540):
            radian+=1
            x=400+300*math.sin(radian/360*2*math.pi)
            y=290+200*math.cos(radian/360*2*math.pi)
        else:
            moving_count-=1
            radian=180
            x=0
            y=90
        delay(0.001)
close_canvas()




