import random

randomlist = []

for i in range(0, 3000):
    n = random.randint(1, 500)
    randomlist.append(n)

print(randomlist)