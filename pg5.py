 #Let's play hangman game
l=["  +----+","       |","       |","       |","     - - -","     - - -"]
s1="    o  |"
s2="   /   |"
s3="   /|  |"
s4="   /|\ |"
s5="   /   |"
s6="   / \ | "
s7="       _ _ _"
s8="       _ _ _"
word="y a h h o o"
re="_ a _ h _ _"
n=10
rc=""
f=0
c=0
size=len(l)-3
print("BEFORE GAME:")
for i in l:
      print(i)
while n>0:
    n=n-1
    x=input("Enter a letter:")
    if x in word:
        for j in range (len(word)):
            if x==word[j] and re[j]=="_":
                re=re[:j]+x+re[j+1:]
                print(re)
                break
        for i in l:
            print(i)
    else:
        rc=rc+x+" "
        print(re)
        print("Missed letters: ",rc)
        print("No. of gusess left :",n)
        c=c+1
        if c==1:
            l[c]=s1
            for i in l:
                print(i)
        elif c==2:
            l[2]=s2
            for i in l:
                print(i)
        elif c==3:
            l[2]=s3
            for i in l:
                print(i)
        elif c==4:
            l[2]=s4
            for i in l:
                print(i)
        elif c==5:
            l[3]=s5
            for i in l:
                print(i)
        elif c==6:
            l[3]=s6
            for i in l:
                print(i)
            break
    if re==word:
        f=1
        break
if f==1:
    print("you won!!")
else:
    print("You lost!!")
    print("Better luck next time!!")
  


