r = 1
area = 2

def numset():
    global r
    r = float(input("what is the radius of your circle?:"))
def calcArea():
    global area
    area = (r*r)*3.14

numset()
calcArea()

print(area)
