s = input()
sub = input()

diff = len(s) - len(sub)
ans = 10000
for i in range(diff + 1):
    temp = 0
    for idx in range(len(sub)):
        if s[idx+i] != sub[idx]:
            temp += 1
    ans = min(ans, temp)

print(ans)
