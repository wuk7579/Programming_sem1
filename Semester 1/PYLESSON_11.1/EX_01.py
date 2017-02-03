class car:
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t
    def setcustom(self, newPaint, newInterior, newEngine, newTire):
        self.paint = newPaint
        self.interior = newInterior
        self.engine = newEngine
        self.tires = newTire
    def getpaint(self):
        return self.paint
    def getinterior(self):
        return self.interior
    def getengine(self):
        return self.engine
    def gettire(self):
        return self.tires
def main():
    paint = input("please enter a paint color:")
    interior = input("please enter an interior:")
    engine = input("please enter an engine:")
    tire = input("please enter a tire:")
    feature = car(paint, interior, engine, tire)
    print("your vehicle is ready....")
    print("paint", feature.getpaint())
    print("interior", feature.getinterior())
    print("engine", feature.getengine())
    print("tire", feature.gettire())
main()
