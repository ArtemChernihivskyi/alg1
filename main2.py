def sum_digits(n):
    return sum(int(d) for d in str(n))

for i in range(1, 1000000):  
    if i == 26 * sum_digits(i):
        print(i)