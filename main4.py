def move_last_to_front(n):
    s = str(n)
    return int(s[-1] + s[:-1])

for i in range(10, 1000000):
    if move_last_to_front(i) == 5 * i:
        print(i)
        break