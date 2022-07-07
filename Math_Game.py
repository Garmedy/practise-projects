import random
import time

print("        Simple Math Game\n")
time.sleep(2)
print("       What do you prefer?\n")
time.sleep(1)
print("      Please type the number\n")
time.sleep(1)
def answer():
    print("        1 : +     3 : *\n        2 : -     4 : / \n")
    global ans
    ans = int(input("              "))
    time.sleep(1)
    if ans >= 5:
        print("\n    There is no such equation \n          in the list\n")
        time.sleep(1)
        print("        Please try again\n")
        time.sleep(1)
        answer()
    else:
        print("\n        Let's continue\n")
        time.sleep(1)
answer()

if ans == 1:
    ans = ("+")
elif ans == 2:
    ans = ("-")
elif ans == 3:
    ans = ("*")
elif ans == 4:
    ans = ("/")

dt1= ("1234567890")
dt2=("10" , "20" , "30" , "40" , "50" , "60" , "70" , "80" , "90", "00")
dt3=("100", "200" , "300" , "400" , "500" , "600" , "700" , "800" , "900" , "000" )

print("    How many you want to answer?\n")
sen = int(input("              "))
time.sleep(1)
print("\n        How many digit the \n         question will be?\n")
time.sleep(1)
def digit():
    print("    1 : 0     2 : 00    3 : 000\n")
    global den
    den = int(input("              "))
digit()
for i in range (sen):
    if den >= 4:
        time.sleep(1)
        print("      I only have numbers \n        less than 999\n")
        digit()
    elif den == 1:
        que = int(random.choice(dt1))
        qui = int(random.choice(dt1))
        print("\n            ",que, ans, qui)
        sag = float(input("\n            "))
        if sag == que + qui or sag == que - qui or sag == que * qui or sag == que / qui:
            print("        you got it right")
        else:
            print("        you are wrong")
    elif den == 2:
        qu = (random.choice(dt1))
        qu1 = int(random.choice(dt2))
        qi = (random.choice(dt1))
        qi1 = int(random.choice(dt2))
        que = int(qu) + int(qu1)
        qui = int(qi) + int(qi1)
        print("\n          ",que, ans, qui)
        sag = float(input("\n            "))
        if sag == que + qui or sag == que - qui or sag == que * qui or sag == que / qui:
            print("        you got it right")
        else:
            print("        you are wrong")
    elif den == 3:
        qu = (random.choice(dt1))
        qu1 = (random.choice(dt2))
        qu2 = (random.choice(dt3)) 
        qi = (random.choice(dt1))
        qi1 = (random.choice(dt2))
        qi2 = (random.choice(dt3))
        que = int(qu) + int(qu1) + int(qu2)
        qui = int(qi) + int(qi1) + int(qi2)
        print("\n          ",que, ans, qui)
        sag = float(input("\n            "))
        if sag == que + qui or sag == que - qui or sag == que * qui or sag == que / qui:
            print("        you got it right")
        else:
            print("        you are wrong")