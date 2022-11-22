import turtle

a = 0
b = 0

turtle.bgcolor("green")
turtle.pencolor("black")
turtle.penup()
turtle.speed(0)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.rigth(b)
    a += 3
    b += 1
    if b == 200:
        break
turtle.exitonclick()