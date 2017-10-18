from random import random

n_samples = 1000000000
hits = 0
for sample in range(n_samples):
    x, y = random(), random()
    if x ** 2 + y ** 2 < 1.0:
        hits += 1

pi = 4 * (hits / n_samples)

print(pi)
