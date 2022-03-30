a, b = input().split()
minlen = min(len(a), len(b))

ans = 'Easy'
for i in range(1, minlen+1):
    if int(a[-i]) + int(b[-i]) >= 10:
        ans = 'Hard'
print(ans)
