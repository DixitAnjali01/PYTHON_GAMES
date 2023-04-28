#let's generate OTP
import random
import string
a=string.digits
b=string.ascii_uppercase
l=a+b
n=6
re=""
while n>0:
    x=random.choice(l)
    re=re+str(x)
    n=n-1
print(re)


