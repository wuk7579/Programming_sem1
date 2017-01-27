import math
class distance:
    def __init__(self, x1, y1, x2, y2):
        self.one = x1
        self.yone = y1
        self.xtwo = x2
        self.ytwo = y2
        self.distance = 0
    def setvalue(self, newx1, newy1, newx2, newy2):
        self.one = newx1
        self.yone = newy1
        self.xtwo = newx2
        self.ytwo = newy2
        self.distance = 0
    def getmph:
        delf.distance = math.sqrt((self.xtwo - self.xone) * (self.xtwo - self.xone)+ (self.ytwo- self.yone) * (self.ytwo-self.yone)
        return self.distance
def main():
    x1 = int(input("Please enter a number for X one:"))
    y1 = int(input("Please enter a number for Y one:"))
    x2 = int(input("Please enter a number for x two:"))
    y2 = int(input("Please enter a number for Y two:"))
    user1 = distance(x1, y1, x2, y2)
    print("Distance = ", user1.getmph())
main()
