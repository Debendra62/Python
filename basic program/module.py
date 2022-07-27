import random as r
a=r.randrange(1,10)
print(a)
b=r.randrange(100)
print(b)
c=r.randrange(0,100,3)
print(c)

options=["win","loose","draw"]
d=r.choice(options)
print(d)
e=r.sample(options,k=2)
print(e)




