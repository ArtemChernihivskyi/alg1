def sum_digits(n):
    return sum(int(d) for d in str(n))


def find_example(k):
    for n in range(1, 10000):
        if sum_digits(n * k) * k == sum_digits(n):
            return n
    return None


for k in range(2, 10):
    print(k, find_example(k))