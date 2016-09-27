

def format(r, p, n, t):
    return(p*(1+r/n)**(n*t))

r = float(input("What is your interest rate?"))
n = float(input("How many times the loan is compouded per year?"))
t = float(input("How many years you spent to pay back the loan?"))
p = float(input("How much money did you borrow?"))


print ("your total cost is",format(r, p, n, t))
