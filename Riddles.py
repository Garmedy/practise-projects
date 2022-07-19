import random
import os
import time

def title_screen():
    print("===================================================================\n")
    print("       ______     _____   ___      ___  ___   ______   _______")
    print("      |  ____|   | ___ |  | |      | |  | |  | _____|  | ___ |")
    print("      \  \____   | | | |  | |      | |  | |  | |__     | |_| |")
    print("       \____  |  | | | |  | |      \ \  / /  |  __|    |  __ /")
    print("       ____/  /  | |_| |  | |____   \ \/ /   | |____   | | \ \ ")
    print("      |______/   |_____|  |______|   \__/    |______|  |_|  \_\ \n")
    
    print("\n===================================================================\n")
    time.sleep(1)
    print("            (0) Play Game            (1) About Game\n\n            (2) About Game Dev       (3) More Info\n\n            (4) Tutorial             (5) Exit Game\n")
title_screen()

def game_category():
    print("===================================================================\n")
    print("                              Riddles\n\n                       consist of 10 riddles")
    print("\n===================================================================\n")
    print("\n                           Enter to start")

def game():
    p_ans = input("                               ")
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    if p_ans not in numbers:
        print("\n                           not a number")
        time.sleep(0.5)
        os.system("clear")
        title_screen()
        game()
    elif p_ans in numbers:
        if p_ans >= "6":
            print("\n                   I don\'t have option for that")
            time.sleep(0.5)
            os.system("clear")
            title_screen()
            game()
        elif p_ans == "0":
            os.system("clear")
            p = 0
            while p <= 100:
                print("\n\n\n                           Generating.....")
                print("\n\n                              ",str(p), '%')
                time.sleep(0.05)
                os.system("clear")
                p += 1
                if p == 100:
                    print("\n\n\n                           Game Generated")
                    print("\n\n                              ",str(p), '%')
                    time.sleep(1)
                    os.system("clear")
            print("\n\n\n                           Game Generated")
            print("\n\n                              ",str(p - 1), '%')
            print("\n\n                            Tap to Enter")
            enter = input("\n                                 ")
            if enter == (""):
                os.system("clear")
                game_category()
            else:
                os.system("clear")
                game_category()
        elif p_ans == '1':
            os.system("clear")
            print("\n\n                          About Game\n")
            print("        The game is design to help the player solve some\n\n         problems and to enhance their memory in riddles.")
            time.sleep(2)
            print("\n\n\n                      Back to Title Screen")
            back = input("                                ")
            if back == "":
                os.system("clear")
                title_screen()
                game()
            else:
                os.system("clear")
                title_screen()
                game()
        elif p_ans == "2":
            os.system("clear")
            print("\n\n                          About Game Dev\n")
            print("      The Game Developer is a 16 years old, as i the game\n\n         developer wants to be a web developer, a game \n\n      developer and a programmer, the first language i learn\n\n     was javascript but something got in my mind that is why\n\n         i didn\'t finish learning the javascript and i switch\n\n                         to learn python.")
            time.sleep(2)
            print("\n\n\n                      Back to Title Screen")
            back = input("                                ")
            if back == "":
                os.system("clear")
                title_screen()
                game()
            else:
                os.system("clear")
                title_screen()
                game()
        elif p_ans == "3":
            os.system("clear")
            print("\n\n                          More Information\n")
            print("                              For Game\n")
            print("         The game is the 7th code that i uploaded in my \n\n      github, it is the most cleanest code so far that i made")
            print("\n\n                          For Game Developer\n")
            print("             The game developer is currently at Grade 10,\n\n          living in The Philippines, a 16 year old boy who\n\n                    recently learn basic python.")
            time.sleep(2)
            print("\n\n\n                      Back to Title Screen")
            back = input("                                ")
            if back == "":
                os.system("clear")
                title_screen()
                game()
            else:
                os.system("clear")
                title_screen()
                game()
        elif p_ans == "4":
            os.system("clear")
            print("                           Tutorial")
            print("\n        After the loading screen, the game will begin, always\n\n        remember that the game riddles is limited due to game\n\n       developers knowledge in python, so remembering all the\n\n     riddles that in the game is basically the best thing to do.")
            time.sleep(2)
            print("\n\n\n                      Back to Title Screen")
            back = input("                                ")
            if back == "":
                os.system("clear")
                title_screen()
                game()
            else:
                os.system("clear")
                title_screen()
                game()
        elif p_ans == "5":
            os.system("clear")
            print('\n\n\n\n                                Bye')
            exit()
game()

def categories():
    def riddles():
        r1 = ("\n\n                  how many seconds are in a year?")
        r2 = ("\n\n           I speak without a mouth and hear without ears.\n        I have no body, but I come alive with wind. What am I? ")
        r3 = ("\n\n       What is seen in the middle of March and April that\n      can’t be seen at the beginning or end of either month?")
        r4 = ("\n\n       What English word has three consecutive double letters? ")
        r5 = ("\n\n            What disappears as soon as you say its name? ")
        r6 = ("\n\n                     What gets wet while drying? ")
        r7 = ("\n\n                    What comes once in a minute,\n          twice in a moment, but never in a thousand years?")
        r8 = ("\n\n               Which word in the dictionary is always\n                        spelled incorrectly?")
        r9 = ("\n\n         David’s father has three sons: Snap, Crackle and....? ")
        r10 = ("\n\n             You always find me in the past, I can be\n         created in the present, but the future can never\n                       taint me. What am I?")
        que = random.randint(1, 10)
        
        if que == 1:
            print(r1)
            ans = input("\n\n                               ")
            if ans == "12":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 2:
            print(r2)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "echo" or ans == "echos":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system
                    title_screen()
                    game()
                    categories()
                    
        elif que == 3:
            print(r3)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "letter r" or ans == "r":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system()
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 4:
            print(r4)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "bookkeeper":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 5:
            print(r5)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "silence":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 6:
            print(r6)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "towel":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 7:
            print(r7)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "m" or ans == "letter m":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 8:
            print(r8)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "incorrectly":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 9:
            print(r9)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "david":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
        elif que == 10:
            print(r10)
            ans = input("\n\n                               ")
            ans = ans.lower()
            if ans == "history":
                print("\n                            correct")
            else:
                print("\n                             wrong")
            print("\n                Do you want to try play again? Y|N")
            again = input("\n                                ")
            if again == "Y" or again == "y":
                os.system("clear")
                riddles()
            elif again == "N" or again == "n":
                print("\n                Do you wish to change the game? Y|N")
                pin = input("\n\n                               ")
                if pin == "Y" or pin == "y":
                    os.system("clear")
                    game_category()
                    categories()
                elif pin == "N" or pin == "n":
                    os.system("clear")
                    title_screen()
                    game()
                    categories()
                    
    play = input ("\n         ")
    if play == (" "):
        os.system("clear")
        riddles()
        categories()
    else:
        os.system("clear")
        riddles()
        categories()
        
categories()