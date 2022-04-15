n = int(input())
s = input()

s += '-'
occurence = []
conti = 1
for i in range(n):
    if s[i+1] == s[i]:
        conti += 1
    else:
        occurence.append(conti)
        conti = 1

occurence.append(conti)
ans = 0
for n in occurence:
    ans += (n * (n-1) // 2)
print(ans)
