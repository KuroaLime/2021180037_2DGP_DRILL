import turtle


PenWrite = 6

first_width=300
first_vertical=-300

direction = 0

while(PenWrite>0):
    turtle.penup()
    turtle.goto(-300,first_width)
    turtle.pendown()
    
    turtle.forward(500)
    
    first_width-=100
    PenWrite-=1

turtle.left(270)
PenWrite = 6

while(PenWrite>0):
    turtle.penup()
    turtle.goto(first_vertical,300)
    turtle.pendown()

    turtle.forward(500)
        
    first_vertical+=100
    
    PenWrite-=1

turtle.exitonclick()
