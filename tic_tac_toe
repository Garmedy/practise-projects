import time
import random
import os
move = {1 : "-" , 2 : "-" , 3 : "-" , 4 : "-" , 5 : "-" , 6 : "-" , 7 : "-" , 8 : "-" , 9 : "-"}
table = ( f"| {move[1]} | {move[2]} | {move[3]} |\n| {move[4]} | {move[5]} | {move[6]} |\n| {move[7]} | {move[8]} | {move[9]} |")
number = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
player = []
computer = []
addp = player.append
addc = computer.append
erase = number.remove

print(table)
fine = True
while fine:
    hi = len(number)
    try:
        global start
        start = int(input("enter 1 - 9:\n"))
    except ValueError:
        print("that's not a number, try again")
        time.sleep(1)
        os.system("clear")
        print(table)
    if start > 9:
        print("that number is too large, try again")
        time.sleep(1)
        os.system("clear")
        print(table)
    elif start < 1:
        print("that number is too small, try again")
        time.sleep(1)
        os.system("clear")
        print(table)
    elif start in number:
        erase(start); addp(start); move[start] = "x"
        os.system("clear")
        table = ( f"| {move[1]} | {move[2]} | {move[3]} |\n| {move[4]} | {move[5]} | {move[6]} |\n| {move[7]} | {move[8]} | {move[9]} |")
        print(table)
        ai = random.choice(number)
        erase(ai); addc(ai); move[ai] = "o"
        os.system("clear")
        table = ( f"| {move[1]} | {move[2]} | {move[3]} |\n| {move[4]} | {move[5]} | {move[6]} |\n| {move[7]} | {move[8]} | {move[9]} |")
        print(table)
        if move[1] == "x" and move[2] == "x" and move[3] == "x" or move[4] == "x" and move[5] == "x" and move[6] == "x" or move[7] == "x" and move[8] == "x" and move[9] == "x" or move[1] == "x" and move[4] == "x" and move[7] == "x" or move[2] == "x" and move[5] == "x" and move[8] == "x" or move[3] == "x" and move[6] == "x" and move[9] == "x" or move[1] == "x" and move[5] == "x" and move[9] == "x" or move[3] == "x" and move[5] == "x" and move[7] == "x" :
            print("player win")
            fine = False
        elif move[1] == "o" and move[2] == "o" and move[3] == "o" or move[4] == "o" and move[5] == "o" and move[6] == "o" or move[7] == "o" and move[8] == "o" and move[9] == "o" or move[1] == "o" and move[4] == "o" and move[7] == "o" or move[2] == "o" and move[5] == "o" and move[8] == "o" or move[3] == "o" and move[6] == "o" and move[9] == "o" or move[1] == "o" and move[5] == "o" and move[9] == "o" or move[3] == "o" and move[5] == "o" and move[7] == "o" :
            print("computer win")
            fine = False
        elif hi == 3:
            print("can't go on,\neither tie or you win")
            fine = False
            
