numbers = [1, 6, 8, 1, 2, 1, 5, 6]
def TimeNumber(n):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == n:
            count += 1
    return count

number = int(input("program to count number occurrences in a list \n enter a number? "))
print("{0} appears {1} times in my list".format(number, TimeNumber(number)))
