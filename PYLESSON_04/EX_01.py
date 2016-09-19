

print ("{:>>20}{:<<15}".format("receipt",""))



def printf(word, number):
    print("*{:>15} .... \t{:10.2f}".format(word, number))

word = " Cheese Sandwich"
number = 4.50

printf(word, number)

word = "French Fires"
number = 4.50

printf(word, number)

word = "soda"
number = 4.50

printf(word, number)

word = "\n\tSubtotal:"
number = 9.01

printf(word, number)

word = "Tax:"
number = 0.63

printf(word, number)

word = "Total:"
number = 9.64

printf(word, number) 

print ("{:_<20}{:_>20}".format("_", ""))
print ("* Thank you for your support*")

       
