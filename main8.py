for i in range(10, 100000):
    s = str(i)
    moved = int(s[-1] + s[:-1])

    if moved == 2 * i:
        print(i)
        break