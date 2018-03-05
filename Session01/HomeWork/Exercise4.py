from turtle import*
shape("turtle")
speed(-1)
color("blue")
fillcolor("yellow")
begin_fill()
#A square
for i in range(4):
    forward(100)
    left(90)

penup()
goto(200,0)
pendown()

#A right triangle
for i in range(3):
    forward(120)
    left(120)


penup()
home()
goto(0,-150)
pendown()

#A circle
circle(50)

end_fill()

penup()
goto(100,-200)
pendown()
#Multi-circles
for i in range(8):
    circle(27)
    left(360/8)

penup()
goto(300,-150)
pendown()
#Or even better
for i in range(25):
    circle(27)
    left(360/25)
mainloop()
