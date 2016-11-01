
number = int(input("Please enter a number:"))
sum = 0
num = number


while num > 0:
    sum = (num %10 + number)
    print(sum)
    num = int(sum/ 10)

print("The sum of the digits in",number," is ", sum)

