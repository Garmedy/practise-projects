import time
import random

lett = "abcdefghijklmnopqrstuvwxyz"
ulett = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"

print ("Password Generator\n")
time.sleep(0.5)
print("Enter how much length you want\n")
pas = lett + num + ulett
x = int(input("    "))
time.sleep(1)
print("\nHow many password do you want to generate?\n")
many = int(input("    "))
time.sleep(1)
print("\nPassword generating")
time.sleep(1)
print("    Please Wait\n")
time.sleep(1)

for i in range(many):
    res = "".join(random.sample(pas , x))
    time.sleep(2)
    print ("     " ,res)
    
print("\nPassword generated")
time.sleep(1)
print("    Thank You")
