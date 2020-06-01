import random

l = [1,2,3,4,5]
r = random.Random(500) # seed number is arbitrary 
o=r.choice(l)
print(r)
i=r.choice(l)

print(o)
print(i)