def is_prime(num):
    if num == 1:
        raise ValueError("error!")
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True

n = int(input())
for i in range(n, n+1000):
    if is_prime(i):
        print(i)
        exit()
