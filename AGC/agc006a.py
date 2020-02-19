a, b, c = list(map(int, input().split()))

if (a * b * c) % 2 == 0:
    print(0)
else:
    # 小さいふたつをかけたもの
    print(a * b * c // max(a, b, c))  # /はfloatになるので不可！

# 解説はmin(a*b, b*c, c*a) 別にそれでも良かったな。
