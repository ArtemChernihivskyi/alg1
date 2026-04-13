def sum_digits(n):
    return sum(int(d) for d in str(n))

def exists_solution(k):
    for n in range(1, 1000000):
        if n == k * sum_digits(n):
            return True
    return False


k = 1
while True:
    if not exists_solution(k):
        print("Answer:", k)
        break
    k += 1