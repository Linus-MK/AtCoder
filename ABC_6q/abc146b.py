import string
upper = string.ascii_uppercase

n = int(input())
s = input()
ans = ''
for ch in s:
    idx = upper.find(ch)
    changed = upper[(idx+n)%26]
    ans += changed

print(ans)
