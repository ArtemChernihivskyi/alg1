import time

t0 = time.time()
c = len([i for i in range(1, 1000000 + 1) if i % 3 == 0 and i % 2 != 0])
t = time.time() - t0

print("count:", c, "time:", t)