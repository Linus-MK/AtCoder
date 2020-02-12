s = input()
ans = 0
count = 0
for i in range(len(s)):
    if s[i] == 'W':
        ans += i - count
        count += 1
print(ans)
