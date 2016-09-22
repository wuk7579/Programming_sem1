

def printf(word, year):
    print("*{:>12}\t{:>16}*".format(word, year))

lname = input("please enter your last name:")
fname = input("Please enter your first name:")
year = input("Please enter the school year:")
school = input("Which school do you go to?")
subject = input("What is your subject?")
title = input("Enetr your title:")

print ("{:*^40}".format(""))

printf(school, year)
printf(fname, lname)
printf(title, subject)

print ("{:*^40
       }".format(""))

