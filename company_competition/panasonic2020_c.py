# 式を普通に実装すると浮動小数点で死ぬ

a, b, c = list(map(int, input().split()))

if (c - a - b > 0) and (4 * a * b < (c - a - b) ** 2):
    print('Yes')
else:
    print('No')
