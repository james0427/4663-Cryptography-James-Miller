import random
from pprint import pprint

seed =500000

chars ='ABCDEFGHIJKLMNO'

#print(chars)
size = len(chars)


def buildVigenere(chars):
    random.seed(seed)
    vigenere = [[0 for i in range(size)] for i in range(size)]
    chars = list(chars)
    random.shuffle(chars)
    chars =''.join(chars)

    for sym in chars:
        random.seed(seed)
        myList =[]
        for i in range(size):
            r = random.randrange(size)
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(size)
                myList.append(r)
            while(vigenere[i][r] != 0):
                r = (r + 1) % size
            vigenere[i][r] = sym
    return vigenere

pprint(buildVigenere(chars))
