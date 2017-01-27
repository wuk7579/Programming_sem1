class human:
    def _init__(self, h, e, s):
        self.hair = h
        self.eye = e
        self.skin = s
    def sethes(self, newhpair, neweye, newskin):
        self.hair = newhair
        self.eye = neweye
        self.skin = newskin
    def gethair(self):
        return self.hair
    def geteye(self):
        return self.eye
    def getskin(self):
        return self.skin
def main():
    hair = input("enter your hair color")
    eye = input("enter your eye color")
    skin = input("enter your skin color")
    personalities = human(hair,eyes, skin)
    print("My info.....")
    print("Hair: black")
    print("eyes: black")
    print("skin: yellow\n\n")

    print("Your info....")
    print("Hair:", personalites.gethair())
    print("Eye:", personalites.geteye())
    print("skin:", personalites.getskin())
main()
