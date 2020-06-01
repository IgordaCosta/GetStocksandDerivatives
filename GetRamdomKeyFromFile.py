import os
import random


def GetRandomKey(filename,randomKey='no'):
    os.chdir(os.path.dirname(__file__))

    lines=open(filename).read()
    print(lines)
    linesList=list(lines)
    #keys=random.choice(lines)

    keys = ''.join(random.sample(linesList, len(linesList)))
    
    print(keys)
    if randomKey=='yes':
        return keys
    else:
        return lines

# Keys=GetRandomKey(filename='keys.txt',randomKey='no')

# print(Keys)