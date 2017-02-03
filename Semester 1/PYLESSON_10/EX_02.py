go = input("Please enter 16 strings:")
spList = go.split(" ")
wordlist = []
spot = 0

for i in range(0, 4):
    output = ""
    wordlist.append([])
    for j in range(0, 4):
        wordlist[i].append(spList[spot])
        output+= wordlist[i][j]+" "
        spot += 1
    print(output)
