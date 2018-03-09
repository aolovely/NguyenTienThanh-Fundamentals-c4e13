from turtle import*
shape("arrow")
speed(-1)
mau = ["red", "blue", "brown", "yellow", "grey"]
for i in range(3, 8, 1):
    color(mau[i-3])
    for j in range(i):
        forward(90)
        left(360/i)
mainloop()
