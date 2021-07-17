# 計算でO(1)で直接答えを求めることも可能だが、別にしなくてもよい。
a, b, c, d = list(map(int, input().split()))

blue = a
red = 0

for i in range(100000):
    blue += b
    red += c
    if red * d >= blue:
        print(i+1)
        exit()
print(-1)
