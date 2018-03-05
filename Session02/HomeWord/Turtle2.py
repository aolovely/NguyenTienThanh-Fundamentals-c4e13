from turtle import*
shape("arrow")
speed(-1)
n = 6
for i in range(3, n+1):
    if i == 3 or i == 5:
        color("blue")
    else:
        color("red")
    for j in range(i):
        forward(90)
        left(360/i)
mainloop()
