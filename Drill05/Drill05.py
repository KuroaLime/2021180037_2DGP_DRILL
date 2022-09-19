import turtle

turtle.shape("turtle")

def move_forward():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
    
def move_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
    
def move_behind():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)
    
def move_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
        
def restart():
    turtle.reset()



turtle.onkey(move_forward,'w')
turtle.onkey(move_left,'a')
turtle.onkey(move_behind,'s')
turtle.onkey(move_right,'d')

turtle.onkey(restart,'Escape')
turtle.listen()

turtle.exitonclick()
