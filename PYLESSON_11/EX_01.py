class milesperhour:
    def __init__(self, d, h, m):
        self.distance = d
        self.hour = h
        self.minute = m
        self.mph = 0
    def setvalue(self, newdistance, newhour, newminute):
        self.distance = newdistance
        self.hour = newhour
        self.minute = newminute
        self.mph = 0
    def getdist(self):
        return self.distance
    def gethour(self):
        return self.hour
    def getmin(self):
        return self.minute
    def getmph(self):
        self.mph = self.distance/(self.hour+self.minutes/60.0)
        retrun self.mph

def main():
    distance = int(input("Please enter the distance:"))
    hour = int(input("please enter the hours:"))
    minute = int(input("Please enter the minutes:"))
    user1 = milesperhour(distance,hour,minute)
    print(user1.getdist()"miles in", user1.gethour(),"hours and", user1.getmin(), "MInutes =", user1.getmph(),"mph")

main() 
