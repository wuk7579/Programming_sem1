
print("Please put all your letter grade in capital.")
one = input("please enter the letter grade in your first class:")
two = input("please enter the letter grade in your second class:")
three = input("please enter the letter grade in your third class:")
four = input("please enter the letter grade in your fourth class:")
five = input("please enter the letter grade in your fifth class:")
six = input("please enter the letter grade in your sixth class:")
seven = input("please enter the letter grade in your seventh class:")

def calcPoint(grd):
    if grd == "A":
        return 4.0;
    if grd == "B":
        return 3.0;
    if grd == "C":
        return 2.0;
    if grd == "D":
        return 1.0;
    if grd == "F":
        return 0.0;
    
g1 = calcPoint(one)
g2 = calcPoint(two)
g3 = calcPoint(three)
g4 = calcPoint(four)
g5 = calcPoint(five)
g6 = calcPoint(six)
g7 = calcPoint(seven)

print("your GPA is ", (g1 + g2 + g3 + g4 + g5 + g6 + g7)/7)

