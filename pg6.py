#Generate password
import random
import string
x=string.digits
y=string.ascii_letters
n=8
re=[]
rc=""
while n>0:
    z=random.choice(x)
    re.append(z)
    n=n-1
n=4
while n>0:
    z=random.choice(y)
    w=random.randrange(1,len(re))
    re.insert(w,z)
    n=n-1
for i in re:
    rc=rc+str(i)
print(rc)

