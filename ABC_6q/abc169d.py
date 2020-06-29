n = int(input())

if n == 1:
    print(0)
    exit()

def is_prime(num):
    if num == 1:
        raise ValueError("error!")
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False, d
        d += 1
    return True, -1


x = n
yakusuu = {}
while True:
    x_is_prime, div = is_prime(x)
    if x_is_prime:
        yakusuu[x] = yakusuu.get(x, 0) + 1
        break
    else:
        yakusuu[div] = yakusuu.get(div, 0) + 1
        x = x // div

# print(yakusuu)
ans = 0
for v in yakusuu.values():
    for p in range(1, 10000):
        if p*(p+1)//2 <= v < (p+2)*(p+1)//2:
            ans += p
            break
print(ans)
