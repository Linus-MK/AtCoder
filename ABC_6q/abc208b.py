n = int(input())

ans = 0
for i in range(2,12):
    ans += n % i
    n //= i
print(ans)
