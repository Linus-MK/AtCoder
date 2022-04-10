s = input()

s_max = s
s_min = s
for i in range(len(s)):
    s = s[1:] + s[0]
    s_max = max(s, s_max)
    s_min = min(s, s_min)

print(s_min)
print(s_max)
