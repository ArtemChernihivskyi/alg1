import time
import math
import random


# 1. Сумма делителей (без самого числа)


def sum_divs(n):
    s = 1

    if n == 1:
        return 0

    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            s += d

            if d != n // d:
                s += n // d

    return s


# Проверка
for i in range(1, 21):
    print(i, "->", sum_divs(i))



# 2. Какие числа встречаются чаще?

# deficient  -> сумма делителей < числа
# abundant   -> сумма делителей > числа
# perfect    -> сумма делителей = числа

def classify(n):
    s = sum_divs(n)

    if s < n:
        return "deficient"

    elif s > n:
        return "abundant"

    else:
        return "perfect"


cnt_def = 0
cnt_ab = 0
cnt_perf = 0

for i in range(1, 1000001):

    t = classify(i)

    if t == "deficient":
        cnt_def += 1

    elif t == "abundant":
        cnt_ab += 1

    else:
        cnt_perf += 1

print("\nОт 1 до 1 000 000:")
print("Недостаточные:", cnt_def)
print("Избыточные:", cnt_ab)
print("Совершенные:", cnt_perf)



# 3. Совершенные числа


perfect_numbers = []

for i in range(1, 100000000):
    if sum_divs(i) == i:
        perfect_numbers.append(i)

        print("Совершенное число:", i)

        if len(perfect_numbers) >= 8:
            break



# 4. Дружественные числа


for a in range(2, 100000):

    b = sum_divs(a)

    if b > a:
        if sum_divs(b) == a:
            print("\nДружественная пара:")
            print(a, b)



# 5. Цепочки из 3,4,5 чисел


def chain(start, length):

    arr = [start]

    cur = start

    for _ in range(length - 1):
        cur = sum_divs(cur)
        arr.append(cur)

    return arr


for i in range(2, 50000):

    c3 = chain(i, 3)

    if sum_divs(c3[-1]) == i:
        print("\nЦепочка из 3:")
        print(c3)
        break



# 6. Наивный алгоритм НОД


def listdivs(N):

    res = []

    for d in range(1, int(math.sqrt(N)) + 1):

        if N % d == 0:

            res.append(d)

            if N // d != d:
                res.append(N // d)

    return res


def NOD(A, B):

    divsA = listdivs(A)
    divsB = listdivs(B)

    res = 1

    for d in divsA:

        if d in divsB:

            if d > res:
                res = d

    return res


ranges = [
    (1_000_000, 2_000_000),
    (10_000_000, 20_000_000),
    (100_000_000, 200_000_000)
]

print("\nНаивный НОД:")

for L, R in ranges:

    t0 = time.time()

    for i in range(1000):

        A = random.randint(L, R)
        B = random.randint(L, R)

        C = NOD(A, B)

    t = time.time() - t0

    print(L, "-", R, ":", t)



# 7. Алгоритм Эвклида


def euclid(a, b):

    while b != 0:
        a, b = b, a % b

    return a


print("\nАлгоритм Эвклида:")

for L, R in ranges:

    t0 = time.time()

    for i in range(1000):

        A = random.randint(L, R)
        B = random.randint(L, R)

        C = euclid(A, B)

    t = time.time() - t0

    print(L, "-", R, ":", t)



# Вывод

print("""
Сложность алгоритма Эвклида примерно логарифмическая:
O(log n)

Он работает намного быстрее наивного метода,
потому что не ищет все делители числа.
""")

