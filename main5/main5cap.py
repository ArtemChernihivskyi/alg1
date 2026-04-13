import time

def count_numbers(n):
    total = n // 3      
    even = n // 6       
    return total - even 

t0 = time.time()
c = count_numbers(1000000)
t = time.time() - t0

print("count:", c, "time:", t)