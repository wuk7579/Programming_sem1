

number = int(input("Please enter the integer of the table:"))
size = int(input("Please enter the size of the table:"))

def graph():
    for i in range(1,size+1):
        print("{:5}\t|{:5}".format(i ,number * i))

graph()
