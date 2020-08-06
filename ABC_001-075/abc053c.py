# 6, 5, 6, 5, ...

x = int(input())
q = x // 11
r = x % 11
if r == 0:
    ans = q * 2
elif 1 <= r <= 6:
    ans = q * 2 + 1
elif 7 <= r <= 10:
    ans = q * 2 + 2
print(ans)
