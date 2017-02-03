
sentence = input("Please enter a sentence:")
top = 0

def replace(sent):
    if sent.count(" ") == 0:
        return sent
    else:
        return replace(sent[0 : sent.index(" ")]+ "_" + sent[sent.index(" ")+1: len(sent)])

print(replace(sentence))
        
