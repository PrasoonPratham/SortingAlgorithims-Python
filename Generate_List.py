import random
import pickle

randomlist = []

for i in range(0, 3000):
    n = random.randint(1, 500)
    randomlist.append(n)

pickle.dump( randomlist, open( "save.p", "wb" ) )