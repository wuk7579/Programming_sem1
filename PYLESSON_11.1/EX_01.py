class car:
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires =t
    def setcustom(self, newpaint, newinterior, newengine, newtire):
        self.paint = newpiant
        self.interior = newinterior
        self.engine = newengine
        self.tires = newtire
    def getpaint(self):
        return self.paint
    def get tinterior(self):
        return self.interior
    def getengine(self):
        return self.engine
    def gettire(self):
        return self.tire
def main():
    paint = int(input("please enter a paint color:"))
    interior = input("please enter an interior:")
    engine = input("please enter an engine:")
    tire = input("please enter a tire:")
    feature = car(piant, interior, engine, tire)
    print("your vehicle is ready....")
    print("paint", feature.getpaint())
    print("interior", feature.getinterior())
    print("engine", feature.getengine())
    print("tire", feature.gettire())
main()
