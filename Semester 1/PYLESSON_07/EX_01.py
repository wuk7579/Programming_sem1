
number = int(input("Please enter a number:"))

def sumdigit():
    global sumt
    sumt = 0
    num = number
    while num > 0:
        sumt = sumt + (num % 10)
        num = int(num/10)

sumdigit()
print("The sum of the digits in",number," is ", sumt)

