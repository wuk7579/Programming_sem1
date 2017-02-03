class human:
    def __init__(self, hair, eyes, skin):
        self.hair = hair
        self.eyes = eyes
        self.skin = skin
    def sethes(self, newHair, newEyes, newSkin):
        self.hair = newHair
        self.eyes = newEyes
        self.skin = newSkin
    def gethair(self):
        return self.hair
    def getEyes(self):
        return self.eyes
    def getskin(self):
        return self.skin
def main():
    hair = input("enter your hair color")
    eyes = input("enter your eyes color")
    skin = input("enter your skin color")
    personalities = human(hair, eyes, skin)
    print("My info.....")
    print("Hair: black")
    print("eyes: black")
    print("skin: yellow\n\n")

    print("Your info....")
    print("Hair:", personalities.gethair())
    print("Eye:", personalities.getEyes())
    print("skin:", personalities.getskin())
main()
