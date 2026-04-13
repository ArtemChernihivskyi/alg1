for i in range(10, 100):
    a = i // 10
    b = i % 10
    new = b * 10 + a

    if new == i * 1.75:
        print(i)