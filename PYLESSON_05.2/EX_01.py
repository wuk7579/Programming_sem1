


def recursion():
    choices = int(input(" What would you like to do?" +
                        "\n 1.Play computer" +
                        "\n 2.Review for the test that is on tomorrow"+
                        "\n 3.Handout with friends"))
    if choices == 1:
        computer = input("what do you likes to do on you computer?" +
                         "\n 1.Watch youtube" +
                         "\n 2.play computer games")
        if computer == 1:
            print("Go do some homework kid, stop wasting the time.")
        else:
            print("You got bad grades on your test and you get grounded for 2 week by your parents.")

    if choices == 2:
        review = int(input("what will you do when you are reviewing for the test?"+
                            "\n 1. Only review for the test"+
                            "\n 2. review while playing games"))
        if review == 1:
            print("You got the perfect score on your test.")
        else:
            print(" You got F on the test.")
    if choices == 3:
        play = int(input("what would you do with your friend?"+
                         "\n 1. Watch movie"+
                         "\n 2. play games"))
        if play == 1:
            print("You realized you have no friends, so you just go watch movie by yourself.")
        else:
            print("You play the game with the friends online.")
    else:
        print("Please stop entering the random stuff, and enter the number on the choices")
        recursion()

recursion()
