import random

inputnum = int(input("Please enter any number of your choice: "))
randnum=9

while(inputnum != randnum):
    inputnum = int(input("Please enter any number: "))
    randnum=random.randint(10,15)
print("Good guess")

