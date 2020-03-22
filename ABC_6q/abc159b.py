s = input()
l = len(s)


def is_kaibun(s):
    ans = True
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            ans = False
    return ans

if is_kaibun(s) and is_kaibun(s[0:(l-1)//2]) and is_kaibun(s[(l+1)//2:]):
    print('Yes')
else:
    print('No')
