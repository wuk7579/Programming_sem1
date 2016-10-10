#----items
item1 = input("please enter item1:")
price1 = float(input("please enter the price:"))

item2 = input("please enter item2:")
price2 = float(input("please enter price2:"))

item3 = input("please enter item3:")
price3 = float(input("please enter price3:"))

item4 = input("please enter item4:")
price4 = float(input("please enter the price:"))

subtotal = price1+ price2+ price3+ price4
discnt = 0
tax = subtotal*.08

#----functions
def discount():
    global subtotal, discnt
    if subtotal >= 2000:
        discnt = 0.15
        

    if subtotal < 2000:
        discnt = 0

def format(word, number):
    print("*{:.15} ...... \t{:10.2f}".format(word,number))


def formats(word, number):
    print("*{:.15} ......{:10.2f}".format(word,number))
discount()

print("-----Here is your recipt----")

format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)
formats("subtotal: ", subtotal)
formats("discount: ", discnt)
format("Tax:", tax)
format("Total:", subtotal - discnt + tax)
print("__________________________________")
print ("* Thank you for your support*")
