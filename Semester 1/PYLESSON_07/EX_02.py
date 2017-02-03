
number = int(input("Please enter a number:"))

def avdigits():
    global digit, average, summ
    digit = 0
    num = number
    summ = 0
    while num > 0:
        digit += 1
        summ += (num % 10)
        num = int(num/10)
    average = float(summ / len(str(number)))

avdigits()
        
print("The average of the digit in", number , "is" , average)

