n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

mm = min(a, b, c, d, e)
ans = ((n + mm - 1) // mm) + 4
print(ans)