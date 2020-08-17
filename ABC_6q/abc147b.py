x = input()
ans = 0
for i in range(len(x)//2):
    if x[i] != x[len(x)-1-i]:
        ans += 1

print(ans)
