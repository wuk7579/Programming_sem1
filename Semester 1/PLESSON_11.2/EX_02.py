import random
class inventoryItem:
    def __init__(self, im, itn, ic, ip = ""):
        self.itemmanufacturer = im
        self.itemname = itn
        self.itemcategory = ic
        self.upc = random.randint(1,100000000)
        self.itemprice = ip
    def sethes(self, newitemnaufacturer, newitemname, newitemcategory, newupc, newitemprice):
        self.itemmanufacturer = newitemnaufacturer
        self.itemname = newitemname
        self.itemcategory = newitemcategory
        self.upc = random.randint(1,100000000)
        self.itemprice = newitemprice
    def getitemmanudaturer(self):
        return self.itemmanufaturer
    def getitemname(self):
        return self.itemname
    def getitemcategory(self):
        return self.itemcategory
    def getupc(self):
        return self.upc
    def getitemprice(self):
        return self.itemprice
    def __str__(self):
        return "custom info...\nItem manufacturer" + self.itemmanufacturer + "\nItem name" + self.itemname + "\nitem category" + self.itemcategory + "\nUPC#" + str(self.upc) + "\nItem price"+ str(self.itemprice)
def main():

    im = input("please enter the item manufacuter")
    itn = input("please enter the item name")
    choice = input("Do you want to enter the category and price?(y or n)")
    if choice == "n":
       user1 = inventoryItem(im, itn)
    else:
        ic = input("please enter the item category")
        ip = int(input("please enter the item price"))
        user1 = inventoryItem(im, itn, ic, ip)
    print(user1.__str__())
main()
    
