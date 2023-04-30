#NUMBER GUESS GAME
import random
score=1
while 1:
    x=random.randint(1000,9999)
    y=int(input("ENTER ANY FOUR DIGIT NUMBER:"))
    if x==y:
        print("WELL DONE YOU GUESS IT RIGHT :)!!")
        print("THE NUMBER OF GUESSES YOU TAKE IS :",score)
        break
    else:
        score+=1
    
