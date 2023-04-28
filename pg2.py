#PLAYING ROCK PAPER SCISSOR
#GAME RULES:
#SCISSOR BEATS PAPER
#PAPER BEATS ROCK
#ROCK BEATS SCISSOR
import random
l=["rock","paper","scissor"]
l1=["rock","paper"]
l2=["paper","scissor"]
l3=["rock","scissor"]
t="yes"
while t=="yes":
    x=random.choice(l)
    y=input("Enter your choice:")
    if x in l1 and y in l1:
        if x=="paper":
            print("Computer wins")
        else:
            print("You Wins!!")
    elif x in l2 and y in l2:
        if x=="scissor":
            print("Computer wins")
        else:
            print("You Wins!!")
    elif x in l3 and y in l3:
        if x=="rock":
            print("Computer wins")
        else:
            print("You Wins!!")
    t=input("Wanna play again?? Enter yes or no :")
print("Thanks for playing :)!!")
    
