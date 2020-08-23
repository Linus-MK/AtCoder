p = list(input())

s = sum(map(int, p))
if s % 9 == 0:
    print('Yes')
else:
    print('No')
