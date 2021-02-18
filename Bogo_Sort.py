import pickle
import random
import sys

#Loading List
list = pickle.load(open("list.p", "rb"))
print(f"{len(list)} values")

#Using a 
while True:
    list1 = random.shuffle(list)
    if list1 != sorted(list):
        print("Not sorted")
        pass
    else:
        print("Sorted")
        sys.exit()