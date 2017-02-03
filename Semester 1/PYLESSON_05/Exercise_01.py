import random
prolldice = random.randint(1,6)
crolldice = random.randint(1,6)
print("you rolled a", prolldice)
print("Computer rolled a", crolldice)

if prolldice > crolldice:
    print("You win")

if crolldice > prolldice:
    print("Computer wins")
    
if prolldice == crolldice:
    print("You tie with the computer")
    
