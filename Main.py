#let's build robot Barista

print("Hello, welcome to NetworkChuck Coffee!!!!!!!")

name = input("What's your name?\n")


if name == "Ben":
    print("Your not welcome here Evil Ben!! GET OUT!!!")
    exit()


else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n\n")


print("Hello " + name + ", thank you so much for coming in today!\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 9
elif order == "Cappucino":
    price = 10

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("thank you, Your total is: $" + str(total))

print("Sound good " + name + ", we'll have your " + quantity + " " + order + "s ready for you in a moment.")
