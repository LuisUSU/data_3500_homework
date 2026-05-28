#Week_2_Prog_Challenge_2
from random import *
randnum = randint(0, 100)

print("Random Number: ", randnum)
print("Guess what number I am thinking!")

guess = 0
while guess != randnum:
    guess = int(input("What is your guess?"))
    if guess > randnum:
        print("Nope lower! Guess Again!")
    elif guess < randnum:
        print("Nope! Higher! Guess Again!")

if guess == randnum:
    print("Holy cow! You are a genius! You got it!")