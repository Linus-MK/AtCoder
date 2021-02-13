t = int(input())

for _ in range(t):
    min_, max_ = list(map(int, input().split()))

    temp = max_ - 2 * min_ + 1

    if temp < 0:
        print(0)
    else:
        print(temp* (temp+1) // 2)
