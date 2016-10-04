
num1 = 1
num2 = 2
num3 = 3
Avg = 3

def numset():
    global num1, num2, num3
    num1 = float(input("what is you first numer?:"))
    num2 = float(input("what is your second number?:"))
    num3 = float(input("what is your third number?:"))
def average():
    global Avg
    Avg = (num1+num2+num3)/3

numset()
average()
print(Avg)
