
oneword = input("Please enter a word:")
twoword = input("Please enter a word:")
threeword = input("Please enter a word:")
def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        word= " "+word+" "
        return makeCenter (word)
        
print(makeCenter(oneword))
print(makeCenter(twoword))
print(makeCenter(threeword))
