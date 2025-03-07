import turtle

screen = turtle.Screen()
turtle.screensize(500, 500)
t = turtle.Turtle()
t.speed(0)
screen.bgcolor('tan')


t.penup()
t.goto(-80,15)
t.pencolor('blue')
t.pendown()
t.circle(35)
t.penup()
t.goto(0,15)
t.pencolor('black')
t.pendown()
t.circle(35)
t.penup()
t.goto(80,15)
t.pencolor('red')
t.pendown()
t.circle(35)
t.penup()
t.goto(-40,-10)
t.pencolor('yellow')
t.pendown()
t.circle(35)
t.penup()
t.goto(40,-10)
t.pencolor('green')
t.pendown()
t.circle(35)



t.penup()
t.goto(0,100)
t.pencolor('purple')
t.pendown()
t.write('Winter Olympics',font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(0,-100)
t.pencolor('purple')
t.pendown()
t.write('2026',font=("Arial",30,"bold"),align="center")

















turtle.done()