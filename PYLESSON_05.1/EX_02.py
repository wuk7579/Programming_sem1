weight = float(input("Please enter your weight in pound:"))
height = float(input("please put your height in inches:"))
bmi = 703*(weight/(height**2))

condition = "None"

if bmi < 18.5:
    condition = "underweight"
elif bmi < 25:
    condition = "normal"
elif bmi < 30:
    condition = "overweight"
elif bmi < 35:
    condition = "obese"
elif bmi < 40:
    comdition = "very obese"
else:
    condition = "morbidly obese"
    

print("Your BMI is", bmi )
print("You are", condition)

 
