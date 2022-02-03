import simple_chalk
pi_large = open("pi.txt", "r")

pi = ""
colour_pi = ""

print("""This is a simple game.
Type in as many digits of pi as possible. 
Once you've finished, press enter.

The game will output your results colour coded red if it's
wrong, green if it's correct, red if not.

ENJOY!!!
""")

pi = input("Type your PI!!!\n> ")

for x in range(0, len(pi)):
    if str(pi[1]) != ".":
        print("Psst! Pi is a decimal number")
    if str(pi) == "π":
        print("smart alec. Do it properly XD")
    if pi[x] == pi_large[x]:
        colour_pi += chalk.green(x)
    else:
        colour_pi += chalk.red(x)
    x += 1

print("Your PI")
print(pi)
print("Correct PI")
print(pi_large[0,len(pi)])

print("MASSIVE PI MWAHAHAHAHAHA!!!!!!")
print(pi_large)
print("P.S. Sorry if your computer broke <3 :)")