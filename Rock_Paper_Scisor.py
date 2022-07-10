import random

def rock():
    print("\n                              /-------\ ")
    print("                             /   `'    \ ")
    print("                             |         | ")
    print("                             |  ' `    /")
    print("                             \_____^__/\n")
def paper():
    print("\n                              |------|")
    print("                              |      |")
    print("                              |      |")
    print("                              |      |")
    print("                              |______|\n")
def scisor():
    print("\n                              |\  /|")
    print("                              \ \/ / ")
    print("                               \OO/")
    print("                               //\\\ ")
    print("                               O  O\n")
    
print ("                        Rock, Paper, Scisor\n")
print("          /-------\          |------|          |\  /|")
print("         /   `'    \         |      |          \ \/ / ")
print("         |         |         |      |           \OO/")
print("         |  ' `    /         |      |           //\\\ ")
print("         \_____^__/          |______|           O  O\n")
print("                How many times do you want to play?\n")
ans = int(input("                                "))
print("\n                           let\'s start\n")
for i in range (ans):
    p1 = str(input("                       r : Rock    p : Paper\n                            s : Scisor\n\n                                "))
    com = random.randint(1 , 3)
    
    if p1 == "r":
        rock()
    elif p1 == "p":
        paper()
    elif p1 == "s":
        scisor()
        
    if com == 1:
        if p1 == "r":
            rock()
            print("                                tie")
        elif rock() != p1:
            if p1 == "p":
                print("                            computer lose\n")
            elif p1 == "s":
                print("                            player  lose\n")
    elif com == 2:
        if p1 == "p":
            paper()
            print("                                tie")
        elif paper() != p1:
            if p1 == "s":
                print("                            computer lose\n")
            elif p1 == "r":
                print("                            player  lose\n")
    elif com == 3:
            if p1 == "s":
                scisor()
                print("                                tie")
            elif scisor() != p1:
                if p1 == "r":
                    print("                            computer lose\n")
                elif p1 == "p":
                    print("                            player  lose\n")                
    