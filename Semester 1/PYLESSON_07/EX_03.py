
number = int(input("Please enter a number:"))

def reverse():
    global num, rev
    num = number
    rev = 0
    while num > 0:
        rev = ((rev) * 10)+ int(num % 10)
        num = int(num/10)
reverse()
print(number,"reversed is", rev)
