import random
import os
import time

def c():
    os.system("clear")

def main():
    def enem_game():
        enem_1 = (f"""==============================================
||                                          ||
||         *--------------------*           ||
||         |                    |           ||
||         |      ^      ^      |           ||
||         |     / \    / \     |           ||
||         |                    |           ||
||         \_                  _/           ||
||           \_              _/             ||
||             \_          _/               ||
||               \_      _/                 ||
||                 \_  _/                   ||
||                   \/                     ||
||                                          ||
||                                          ||
==============================================""")
    
        enem_2 = (f"""==============================================
||                                          ||
||           |\                /|           ||
||           | \______________/ |           ||
||       ____|                  |____       ||
||      /         /\      /\         \      ||
||      \___     /__)    (__\    ____/      ||
||       ___|                   |____       ||
||      /                            \      ||
||      \____                    ____/      ||
||           |__              __|           ||
||              \__        __/              ||
||                 \__  __/                 ||
||                    \/                    ||
||                                          ||
==============================================""")
    
        enem_3= (f"""==============================================
||                                          ||
||         /\  /\  /\  /\  /\  /\           ||
||        /  \/  \/  \/  \/  \/  \          ||
||        |                      |          ||
||        |      ==      ==      |          ||
||        |       •      •       |          ||
||       /                        \         ||
||      /                          \        ||
||     /                            \       ||
||    /_________     __     _________\      ||
||             |   _/  \_   |               ||
||             | _/      \_ |               ||
||             |/          \|               ||
||                                          ||
==============================================""")
    
        enem_4= (f"""==============================================
||                                          ||
||          {{[|\    _____    /|]}}           ||
||          {{[| \  /     \  / |]}}           ||
||          {{[|  \/       \/  |]}}           ||
||          {{[|               |]}}           ||
||          {{[|   @        @  |]}}           ||
||          {{[|               |]}}           ||
||          {{[|               |]}}           ||
||          {{[|               |]}}           ||
||          {{[|_______________|]}}           ||
||               {{[|     |]}}                ||
||                 \\\   //                  ||
||                  \\\_//                   ||
||                                          ||
==============================================""")
    
        enem_5= (f"""==============================================
||                                          ||
||         [[[[[[[[[[[[|]]]]]]]]]]          ||
||            [|             |]             ||
||            [|   _     _   |]             ||
||          {{[[|  |_|   |_|  |]]}}           ||
||            [|             |]             ||
||        {{[[[[|             |]]]}}          ||
||            [|             |]             ||
||          {{[[|             |]]}}           ||
||            [|             |]             ||
||            [|             |]             ||
||         [[[[[[[[[[[[|]]]]]]]]]]          ||
||           [[[[[[[[[[|]]]]]]]]            ||
||                                          ||
==============================================""")
        def attacks():
            ran = random.randint(1 , 5)
            act = True
            level = 1
            hp = level * 50
            den = 10
            din = 0
            while act:
                c()
                dam = random.randint (din , den)
                if ran == 1:
                    print(enem_1)
                    print("level  : " , level , "          hp : " , hp)
                    print("damage : " , dam , "   critical :  20")
                    att = input("")
                    if att == "" :
                        print(hp)
                        pin = random.randint(1 , 10)
                        if pin == 1:
                            dam += 10
                            hp = hp - dam
                            dam -= 10
                        hp = hp - dam
                        if hp <= 0:
                            c()
                            level = level + 1
                            hp = level * 50
                            for i in range (4):
                                print(enem_1)
                                time.sleep(0.5)
                                c()
                                time.sleep(0.5)
                            ran = random.randint(1 , 5)
                            if level % 5 == 0:
                                den = den + 10
                                din = din + 5
                                
                if ran == 2:
                    print(enem_2)
                    print("level  : " , level , "          hp : " , hp)
                    print("damage : " , dam , "   critical :  20")
                    att = input("")
                    if att == "" :
                        print(hp)
                        pin = random.randint(1 , 10)
                        if pin == 1:
                            dam += 10
                            hp = hp - dam
                            dam -= 10
                        hp = hp - dam
                        if hp <= 0:
                            c()
                            level = level + 1
                            hp = level * 50
                            for i in range (4):
                                print(enem_2)
                                time.sleep(0.5)
                                c()
                                time.sleep(0.5)
                            ran = random.randint(1 , 5)
                            if level % 5 == 0:
                                den = den + 10
                                din = din + 5
                                
                if ran == 3:
                    print(enem_3)
                    print("level  : " , level , "          hp : " , hp)
                    print("damage : " , dam , "   critical :  20")
                    att = input("")
                    if att == "" :
                        print(hp)
                        pin = random.randint(1 , 10)
                        if pin == 1:
                            dam += 10
                            hp = hp - dam
                            dam -= 10
                        hp = hp - dam
                        if hp <= 0:
                            c()
                            level = level + 1
                            hp = level * 50
                            for i in range (4):
                                print(enem_3)
                                time.sleep(0.5)
                                c()
                                time.sleep(0.5)
                            ran = random.randint(1 , 5)
                            if level % 5 == 0:
                                den = den + 10
                                din = din + 5
                                
                if ran == 4:
                    print(enem_4)
                    print("level  : " , level , "          hp : " , hp)
                    print("damage : " , dam , "   critical :  20")
                    att = input("")
                    if att == "" :
                        print(hp)
                        pin = random.randint(1 , 10)
                        if pin == 1:
                            dam += 10
                            hp = hp - dam
                            dam -= 10
                        hp = hp - dam
                        if hp <= 0:
                            c()
                            level = level + 1
                            hp = level * 50
                            for i in range (4):
                                print(enem_4)
                                time.sleep(0.5)
                                c()
                                time.sleep(0.5)
                            ran = random.randint(1 , 5)
                            if level % 5 == 0:
                                den = den + 10
                                din = din + 5
                                
                if ran == 5:
                    print(enem_5)
                    print("level  : " , level , "          hp : " , hp)
                    print("damage : " , dam , "   critical :  20")
                    att = input("")
                    if att == "" :
                        print(hp)
                        pin = random.randint(1 , 10)
                        if pin == 1:
                            dam += 10
                            hp = hp - dam
                            dam -= 10
                        hp = hp - dam
                        if hp <= 0:
                            c()
                            level = level + 1
                            hp = level * 50
                            for i in range (4):
                                print(enem_5)
                                time.sleep(0.5)
                                c()
                                time.sleep(0.5)
                            ran = random.randint(1 , 5)
                            if level % 5 == 0:
                                den = den + 10
                                din = din + 5
                                
        attacks()
    
    main = """==============================================
||                                          ||
||                                          ||
||                                          ||
||              _  _      _                 ||
||             |_|| \\\  /|_ |\ |            ||
||             | ||_/ \/ |_ | \|            ||
||                                          ||
||                                          ||
||                                          ||
||              s ( start game )            ||
||                                          ||
||              q ( quit game )             ||
||                                          ||
||                                          ||
||                                          ||
=============================================="""
    for i in range (3):
        print(main)
        time.sleep(0.3)
        c()
        time.sleep(0.3)
    print(main)
    game = input("")
    if game == "":
        enem_game()
    else:
        exit()
        
main()            