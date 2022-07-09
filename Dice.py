import random

print("            Dice\n")
def dice():
    dc = random.randint(1, 6)
    if dc == 1:
        print("\n        --------------")
        print("        |            |")
        print("        |            |")
        print("        |      o     |")
        print("        |            |")
        print("        |            |")
        print("        --------------")
        
    elif dc == 2:
        print("\n        --------------")
        print("        |            |")
        print("        |  o         |")
        print("        |            |")
        print("        |         o  |")
        print("        |            |")
        print("        --------------")
        
    elif dc == 3:
        print("\n        --------------")
        print("        |            |")
        print("        |  o         |")
        print("        |     o      |")
        print("        |        o   |")
        print("        |            |")
        print("        --------------")
        
    elif dc == 4:
        print("\n        --------------")
        print("        |            |")
        print("        |   o    o   |")
        print("        |            |")
        print("        |   o    o   |")
        print("        |            |")
        print("        --------------")
        
    elif dc == 5:
        print("\n        --------------")
        print("        |            |")
        print("        |   o     o  |")
        print("        |      o     |")
        print("        |   o     o  |")
        print("        |            |")
        print("        --------------")
        
    elif dc == 6:
        print("\n        --------------")
        print("        |            |")
        print("        |   o    o   |")
        print("        |   o    o   |")
        print("        |   o    o   |")
        print("        |            |")
        print("        --------------")
        
print("      Do you want to roll\n         the dice? y/n\n")
ans = input("              ")
def game():
    if ans == "y":
        dice()
        print("\n    do you want to roll again?\n")
        pns = input("              ")
        if pns == "y":
            game()
        elif pns == "n":
            print("        bye then")
            exit()
    elif ans == "n":
        print("\n        Ok Byeee......")
game()
