
sentence = input("please enter a sentence")

top = 0
def replace():
    global sentence
    while top < sentence.count("a") > 0:
        sentence = sentence[0 : sentence.index("a")]+ "@" + sentence[sentence.index("a")+1: len(sentence)]

replace()
print(sentence)
