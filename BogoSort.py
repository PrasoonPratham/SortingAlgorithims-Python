import pickle
import random

list = pickle.load( open( "list.p", "rb" ) )
print(f"{len(list)} values")

while True:
    list1 = random.shuffle(list)
    if list1 != sorted(list): 
        print("Not sorted")
        pass
    else:
        print("Sorted")