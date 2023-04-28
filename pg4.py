#DICE GAME
import random
choice="y"
l=[]
while choice=="y":
    n=random.randrange(1,7)
    l.append(n)
    print("Dice shows",n)
    choice=input("WANNA CONTINUE?y(yes) and n(no):")
print("The series of numbers which dice shows is :",l)
