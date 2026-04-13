def sumdig(N):
    res = 0
    while N > 0:
        x = N % 10
        res += x
        N = N // 10
    return res


def sumdig_var2(N):
    res = 0
    sN = str(N)
    for x in sN:
        res += int(x)
    return res

import time
import random

def test(n_digits):
    num = int(''.join(str(random.randint(1,9)) for _ in range(n_digits)))

    t0 = time.time()
    sumdig(num)
    t1 = time.time()

    sumdig_var2(num)
    t2 = time.time()

    return (t1 - t0), (t2 - t1)


lengths = [5, 10, 15, 20, 30, 40, 50, 60, 80, 100]

for l in lengths:
    t1, t2 = test(l)
    print(l, t1, t2)