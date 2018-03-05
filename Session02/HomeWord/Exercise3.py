#20 numbers, starting from 0
print(*range(20), end = " ")
print()
#Ask users to enter a number, then print n positive numbers from 0 to n-1:
n = int (input("enter number: "))
print("Ask users to enter a number, then print n positive numbers from 0 to n-1:")
print(*range(n), end = " ")
print()
#1’s and 0’s, consecutively
print("1’s and 0’s, consecutively")
for i in range(10):
    print("1 0", end = " ")
print()
#Ask users to enter a number n, then print n 1’s and 0’s in total consecutively:
print("Ask users to enter a number n, then print n 1’s and 0’s in total consecutively:")
for j in range(n):
    if j%2 == 0:
        print("1", end = "")
    else:
        print("0", end = "")
print()

#9 x 9 numbers (multiplication table)
print("9 x 9 numbers (multiplication table)")
for a in range(1, 10):
    for b in range(1, 10):
        print(a*b, end = " ")
    print()
print()
#Ask user to enter a number n, then print n x n numbers, following multiplication table’s pattern:
print("Ask user to enter a number n, then print n x n numbers, following multiplication table’s pattern:")
for l in range(1, n + 1):
    for m in range (1, n + 1):
        print(l * m, end = " ")
    print()
