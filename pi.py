import simple_chalk
from os import name, system




gameMode = True
pi_large = open("pi.txt", "r") #import large pi

pi = "" #input
colour_pi = "" #set output

print("""This is a simple game.
Type in as many digits of pi as possible. 
Once you've finished, press enter.

The game will output your results colour coded red if it's
wrong, green if it's correct.

ENJOY!!!
""")
while gameMode:
    pi = input("Type your PI!!!\n> ")
    if str(pi[1]) != ".":
        print("Psst! Pi is a decimal number")
    if str(pi) == "π":
        print("smart alec. Do it properly XD")

    for x in range(0, len(pi)):
        if pi[x] == pi_large[x]:
            colour_pi += chalk.green(x)
        else:
            colour_pi += chalk.red(x)
        x += 1

    print("Your PI")
    print(pi)
    print("Correct PI")
    print(chalk.blue(pi_large[0,len(pi)]))
    carryOn = input("""Carry on?
    y/N
    > """)
    if carryOn.lower() == "y":
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")




"""
print("MASSIVE PI MWAHAHAHAHAHA!!!!!!")
print(pi_large)
print("P.S. Sorry if your computer broke <3 :)")"""