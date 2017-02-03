class MilesPerHour:
    def __init__(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0
    def setValues(self, newDistance, newHours, newMinutes):
        self.distance = newDistance
        self.hours = newHours
        self.minutes = newMinutes
        self.mph = 0
    def getDist(self):
        return self.distance

    def getHours(self):
        return self.hours

    def getMins(self):
        return self.minutes

    def getMPH(self):
        self.mph = self.distance/(self.hours + self.minutes / 60.0)
        return self.mph

def main():
    distance = int(input("Please enter the distance:"))
    hours = int(input("please enter the hours:"))
    minutes = int(input("Please enter the minutes:"))

    user1 = MilesPerHour(distance , hours , minutes)
    print(user1.getDist(), "miles in ", user1.getHours(),"hours and", user1.getMins(), "Minutes =", user1.getMPH(),"mph")
    user1.setValues(10, 2, 0)
    print(user1.getDist(), "miles in ", user1.getHours(), "hours and", user1.getMins(), "minutes = ", user1.getMPH(), "mph")

main() 
