from turtle import*
shape("arrow")
speed(-1)
mau = ["red", "blue", "brown", "yellow", "grey"]
for i in range(5):
    color(mau[i])
    fillcolor(mau[i])
    begin_fill()
    for j in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)

mainloop()
