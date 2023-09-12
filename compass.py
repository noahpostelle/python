import turtle
tortle = turtle.Turtle()
tortle.speed(0)
tortle.goto(0, -10)
tortle.circle(10)


for i in range(0, 360, 90):
    tortle.penup()
    tortle.goto(0, 0)
    tortle.setheading(i)
    tortle.pendown()
    tortle.forward(100)
tortle.penup()
tortle.goto(-110, -3)
tortle.write("West", align="center")
tortle.goto(110, -3)
tortle.write("East", align="center")
tortle.goto(0, 100)
tortle.write("North", align="center")
tortle.goto(0, -120)
tortle.write("South", align="center")
tortle.hideturtle()
turtle.done()