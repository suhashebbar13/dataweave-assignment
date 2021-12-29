import random

for i in range(1000000):
    hash = random.getrandbits(32)
    print(hex(hash)[2:])