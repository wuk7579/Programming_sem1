
side = 6
surfarea = 36

def numset():
    global side
    side = float(input("what is the side length of your cube?:"))
def calcSurf():
    global sufarea
    surfarea = (side*side)*6

numset()
calcSurf()

print(surfarea)

