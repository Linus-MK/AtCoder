n = int(input())
st = input()

ans = 1
for i in range(n-1):
    if st[i] != st[i+1]:
        ans += 1
print(ans)
