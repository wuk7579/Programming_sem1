
def woofer(length, height, width):
    return((length* height* width)*0.0057870)

print("all the measurement should put in inches")

length = float(input("what is the lengths of the subwoofer boxes?"))
height = float(input("what is the heights of the subwoofer box?"))
width = float(input("what is the width of the subwoofer box?"))

print("The subwoofer box's volume is" ,woofer(length, height, width)," cube feet")

