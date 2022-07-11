import random
import time

print("===================================================================\n\n                        Welcome to Casino\n\n===================================================================")
time.sleep(1)
print("\n                    Instruction on how to play.")
time.sleep(1)
print("\n\n        1. You will input how many cash you have.")
time.sleep(0.5)
print("\n        2. The computer will ask you how many bet you want.")
time.sleep(0.5)
print("\n        3. After you done betting the game will start.")
time.sleep(0.5)
print("\n        4. You need to guess the number to win.")
time.sleep(0.5)
print("\n        5. The winner\'s bet will be multiplied depending \n                on where he\'s/she\'s playing.")
time.sleep(1)
print("\n\n                            Good Luck")
time.sleep(0.5)
print("\n===================================================================")
time.sleep(1)
print("\n                 Type the number corresponding to \n                     where you want to play.")
time.sleep(0.5)
def place():
    print("\n\n                    where do you want to play?")
    time.sleep(0.5)
    print("\n\n                 (1) normal play  (2x) : 1 to 10")
    time.sleep(0.5)
    print("\n                 (2) hard play    (3x) : 1 to 50")
    time.sleep(0.5)
    print("\n                 (3) intense play (4x) : 1 to 100")
    time.sleep(0.5)
    print("\n===================================================================")
    def play(a, b):
        plays = a
        money = b
        if money is None:
                int(input("\n\n                    How many cash do you have?\n\n                                "))
        if plays == 1:
                ren = random.randint(1 , 10)
                print("\n\n                    for normal play let\'s start\n\n")
                bet = int(input("                              Your bet\n\n                                 "))
                print("\n\n                           Guessing time")
                print("\n                              1 to 10")
                gss = int(input("                                 "))
                if ren == gss:
                   print("\n                              You Win")
                   bet = bet * 2
                   money = money + bet
                   print("                                 " + str(money))
                   print("\n                     Do you want to play again? Y/N")
                   pl = str(input("\n                                  "))
                   if pl == "y" or pl == "Y":
                       play(a, money)
                   elif pl == "n" or pl == "N":
                       print("                    Do you want to change place? Y/N\n")   
                       pk = str(input("\n                                  "))
                       if pk == "y" or pk == "Y":
                           place()
                       elif pk =="n" or pk == "N":
                           print("                    Bye.........")
                elif ren != gss:
                   print("\n                              You Lose")
                   money -= bet
                   print("                                 " + str(money))
                   print("\n                    Do you want to play again? Y/N")
                   pl = str(input("\n                                  "))
                   if pl == "y" or pl == "Y":
                       play(a, money)
                   elif pl == "n" or pl == "N":
                       print("                    Do you want to change place? Y/N\n")   
                       pk = str(input("\n                                  "))
                       if pk == "y" or pk == "Y":
                           place()
                       elif pk =="n" or pk == "N":
                           print("                            Bye.........")
                           exit()
        elif plays == 2:
                ren = random.randint(1 , 50)
                print("\n\n                    for hard play let\'s start\n\n")
                bet = int(input("                              Your bet\n\n                                 "))
                print("\n\n                           Guessing time")
                print("\n                              1 to 50")
                gss = int(input("                                 "))
                if ren == gss:
                   print("\n                              You Win")
                   bet = bet * 3
                   money = money + bet
                   print("                                 " + str(money))
                   print("\n                     Do you want to play again? Y/N")
                   pl = str(input("\n                                  "))
                   if pl == "y" or pl == "Y":
                       play(a, money)
                   elif pl == "n" or pl == "N":
                       print("                    Do you want to change place? Y/N\n")   
                       pk = str(input("\n                                  "))
                       if pk == "y" or pk == "Y":
                           place()
                       elif pk =="n" or pk == "N":
                           print("                    Bye.........")
                elif ren != gss:
                   print("\n                              You Lose")
                   money -= bet
                   print("                                 " + str(money))
                   print("\n                    Do you want to play again? Y/N")
                   pl = str(input("\n                                  "))
                   if pl == "y" or pl == "Y":
                       play(a, money)
                   elif pl == "n" or pl == "N":
                       print("                    Do you want to change place? Y/N\n")   
                       pk = str(input("\n                                  "))
                       if pk == "y" or pk == "Y":
                           place()
                       elif pk =="n" or pk == "N":
                           print("                            Bye.........")
                           exit()
        elif plays == 3:
                ren = random.randint(1 , 100)
                print("\n\n                    for intense play let\'s start\n\n")
                bet = int(input("                              Your bet\n\n                                 "))
                print("\n\n                           Guessing time")
                print("\n                              1 to 100")
                gss = int(input("                                 "))
                if ren == gss:
                   print("\n                              You Win")
                   bet = bet * 4
                   money = money + bet
                   print("                                 " + str(money))
                   print("\n                     Do you want to play again? Y/N")
                   pl = str(input("\n                                  "))
                   if pl == "y" or pl == "Y":
                       play(a, money)
                   elif pl == "n" or pl == "N":
                       print("                    Do you want to change place? Y/N\n")   
                       pk = str(input("\n                                  "))
                       if pk == "y" or pk == "Y":
                           place()
                       elif pk =="n" or pk == "N":
                           print("                    Bye.........")
                elif ren != gss:
                   print("\n                              You Lose")
                   money -= bet
                   print("                                 " + str(money))
                   print("\n                    Do you want to play again? Y/N")
                   pl = str(input("\n                                  "))
                   if pl == "y" or pl == "Y":
                       play(a, money)
                   elif pl == "n" or pl == "N":
                       print("                    Do you want to change place? Y/N\n")   
                       pk = str(input("\n                                  "))
                       if pk == "y" or pk == "Y":
                           place()
                       elif pk =="n" or pk == "N":
                           print("                            Bye.........")
                           exit()
        elif plays >= 4:
            print("\n                    We don't have that place")
            time.sleep(1)
            place()
    def game():
        what_to_play = int(input("\n                                 "))
        money = int(input("\n\n                    How many cash do you have?\n\n                                "))
        play(what_to_play, money)
    game()
place()