height = float(input("what is your height: (cm) "))
weight = float(input("what is your weight: (kg)"))
height /= 100
BMI = weight / (height**2)
print("your BMI = ", BMI)
if BMI < 16:
    print("your are severely underweigh")
elif BMI < 18.5:
    print("you are underweigh")
elif BMI < 25:
    print("you are normal")
elif BMI < 30:
    print("you are overweight")
else:
    print("you are obese")
