wordlist = []
wordlist.append(" " + input("word: ") + " ")
wordlist.append(" " + input("word: ") + " ")
wordlist.append(" " + input("word: ") + " ")
wordlist.append(" " + input("word: ") + " ")
wordlist.append(" " + input("word: ") + " ")

print("In order... \n")
output = ""
for i in wordlist:
    output += (i)
print(output)

print("_______________")
print("Reversed... \n")

def reverse():
    out = ""
    for i in range(len(wordlist)-1,-1,-1):
        out += wordlist[i]
    print(out)

reverse()
