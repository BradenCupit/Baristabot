#Let's Build robot Barista


print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!")

name = input("What is your name?\n")


if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("Your not welcome here Evil Ben!! GET OUT!!!")
        exit()
    else:
        print("Oh, so you're one of those good Bens. Come on in!!")


else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n\n")
