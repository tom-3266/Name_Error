#The game is that the computer "thinks" about a number and we have to guess it.
#On every guess, the computer will tell us if our guess was smaller or bigger than the hidden number.
#The game ends when we find the number.Also Define no of attemps took to find this hidden number.
#(Hidden number lies between 0 - 100)


import random
n = random.randint(0,100)
#print(n)
count = 0
y=0
while y==0:
    x = int(input("\nEnter the guessed number : "))
    count+= 1
    if n == x:
        print("\nYou have guessed the right number in {} attempt".format(count))
        y=1
    elif n>x:
        print("\nYour guess was smaller")
        print("Continue guessing")
        y=0
    elif n<x:
        print("\nYour guess was bigger")
        print("Continue guessing")
        y=0
        