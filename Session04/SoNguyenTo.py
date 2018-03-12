n = int(input("enter a number: "))
ktra = 0

if n == 0:
     print(n, "k la so nguyen to")
if n >= 1 and n <=2:
    print(n, " la so nguyen to")
#
# for i in range(2, n//2):
#     if n %i == 0:
#         ktra = 1
#         break
i = 2
while i <= (n**0.5):
    if n % i == 0:
        ktra == 1
        break
    i += 1
if ktra == 0:
     print(n, " la so nguyen to")
else:
    print(n, "khong la so nguyen to")
