import time

t0 = time.time()
c = 0
for i in range(3, 1000000 + 1, 3): 
    if i % 2 != 0:
        c += 1

t = time.time() - t0
print("count:", c, "time:", t)