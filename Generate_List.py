import random
import pickle

list=[]
for i in range(3000):
    r=random.randint(1,10000000)
    if r not in list: list.append(r)

print(len(list))

pickle.dump( list, open( "save.p", "wb" ) )