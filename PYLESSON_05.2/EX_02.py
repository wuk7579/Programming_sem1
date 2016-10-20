username = input("Setting up your username. Please enter the usename that you like to use:")
password = input("Setting up your password. Please enter the password that you like to use:")

def accouncheck():
    usercheck = input("please enter your username:")
    passcheck = input("please enter your password:")
    
    if username == usercheck and password == passcheck:
        print("your are granted access!")
        
    else:
        if username == usercheck:
            print("your password is incorrect, please try again")
            accouncheck()
        elif password == passcheck:
            print("your username is incorrect, please try again")
            accouncheck()
        else:
            print("Your password and username are incorrect, please try again")
            accouncheck()

accouncheck()
