import random
xandO = []
for i in range(0, 4):
    xandO.append([])
    for j in range(0, 4):
        switch = random.randint(0, 1)
        if switch == 1:
            xandO[i] += "x"
        else:
            xandO[i] += "o"
for t in xandO:
    output = ""
    for t in t:
        output += t + " "
    print(output)
