import random

l = [i for i in range(10)]
print(l)

print(random.choice(l))

random.shuffle(l)

print(l)