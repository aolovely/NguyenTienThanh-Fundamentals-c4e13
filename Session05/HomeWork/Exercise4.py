def rabbit(month):
    if month == 0:
        return 1
    if month == 1:
        return 2
    else:
        return rabbit(month - 1) + rabbit(month - 2)

for i in range(5):
    print("month {0}: {1} pairs of rabbit".format(i, rabbit(i)))
