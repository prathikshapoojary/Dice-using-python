print("This is Dice Rolling game!")
while True:
    import random
    print("Press enter to roll dice")
    input()
    number = random.randint(1, 6)
    if number == 1:
        print(" _______________")
        print("|               |")
        print("|               |")
        print("|       O       |")
        print("|               |")
        print("|_______________|")
    if number ==2:
        print(" _______________")
        print("|               |")
        print("|               |")
        print("|    O    O     |")
        print("|               |")
        print("|_______________|")
    if number ==3:
        print(" _______________")
        print("|               |")
        print("|               |")
        print("|    O  O  O    |")
        print("|               |")
        print("|_______________|")
    if number ==4:
        print(" _______________")
        print("|               |")
        print("|    O    O     |")
        print("|               |")
        print("|    O    O     |")
        print("|_______________|")
    if number ==5:
        print(" _______________")
        print("|               |")
        print("|    O     O    |")
        print("|       O       |")
        print("|    O     O    |")
        print("|_______________|")
    if number ==6:
        print(" _______________")
        print("|               |")
        print("|    O    O     |")
        print("|    O    O     |")
        print("|    O    O     |")
        print("|_______________|")
