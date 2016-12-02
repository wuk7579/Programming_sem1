import random
number = []
for i in range(0, 10):
     number.append(random.randint(1, 100)) 

print("Numbers...")

output = ""
for num in number:
    output += str(num) + " "
print(output)

def average(lst):
    avg = 0
    for num in lst:
        avg += num
    return avg/len(number)

print("________________________")
print("The average of the above number is....", average(number))
