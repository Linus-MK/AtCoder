n = int(input())

ans = 0
for a in range(1, n):
    temp = n // a
    if temp * a == n:
        temp -= 1

    ans += temp
print(ans)

