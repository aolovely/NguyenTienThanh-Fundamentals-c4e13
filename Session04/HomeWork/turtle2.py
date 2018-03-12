from turtle import*
shape("arrow")
speed(-1)
color("blue")

left(90)
for i in range(30):
    for j in range(4):
        forward(i + 15)
        left(90)
    left(15)
mainloop()
