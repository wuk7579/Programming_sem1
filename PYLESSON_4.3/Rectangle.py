length = 5
width = 3
perimeter = 15

def numset():
    global length, width
    length = float(input("what is the length of your rectangle:"))
    width =  float(input("what is the width of your rectangle:"))
def calcPerim():
    global perimeter
    perimeter = (length+width)*2

numset()
calcPerim()

print(perimeter)
