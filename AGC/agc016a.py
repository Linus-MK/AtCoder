s = input()

import string
ans = 9999
for char in string.ascii_lowercase:
    count = 0
    maxi = 0
    for j in range(len(s)):
        if s[j] == char:
            maxi = max(count, maxi)
            count = 0
        else:
            count += 1
        maxi = max(count, maxi)
    ans = min(ans, maxi)

print(ans)
