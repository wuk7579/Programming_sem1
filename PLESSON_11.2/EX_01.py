import random
class user:
    def __init__(self, fname, lname, avat = ""):
        self.firstname = fname
        self.lastname = lname
        self.avatar = avat
        self.userid = random.randint(0, 1000000)
    def sethes(self, newfirstname, newlastname, newavatar):
        self.firstname = newfirstname
        self.lastname = newlastname
        self.avatar = newavatar
        self.userid = random.randint(0, 1000000)
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    def getavata(self):
        return self.avatar
    def __str__(self):
        return "custom info...\nFirst name:" + self.firstname + "\nlast Name:" + self.lastname + "\navatar:" + self.avatar + "\nUser ID#:" + str(self.userid)
def main():
    fname = input("Please enter your first name:")
    lname = input("Please enter your last name:")
    choice  = input("Would youlike touse a public avatar?(y or n):")
    if choice == "n":
        user1 = user(fname, lname)
    else:
        avat = input("enter your avatar please:")
        user1 = user(fname, lname, avat)
    print(user1)
main()
