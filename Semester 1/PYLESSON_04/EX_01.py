
def printf(word, number):
    print("*{:>15} ....... \t{:10.2f}".format(word, number))


item1 = input("please enter item1:")
price1 = float(input("please enter the price:"))


item2 = input("please enter item2:")
price2 = float(input("please enter price2:"))


item3 = input("please enter item3:")
price3 = float(input("please enter price3:"))

subtotal = price1+ price2+ price3
tax = subtotal*.8
total = tax+ subtotal
print ("{:>>25}{:<<20}".format("receipt",""))

printf(item1, price1)
printf(item2, price2)
printf(item3, price3)
print("\n");
printf("subtotal:", subtotal)
printf("Tax:", tax)
printf("Total:", total)
print ("{:_<20}{:_>20}".format("_", ""))
print ("* Thank you for your support*")
