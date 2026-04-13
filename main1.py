def sum_digits(n):
    return sum(int(d) for d in str(n))

for i in range(10, 100):
    if i == 5 * sum_digits(i):
        print(i)