bacterias = int(input("How many B bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))

bacterias = bacterias*(2**(time//2))

print("After {0} minutes, we would have {1} bacterias".format(time, bacterias))
