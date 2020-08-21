# 最大値と最小値を調べておいて、それを掛け合わせる

n = int(input())
left_heights = list(map(int, input().split()))
right_heights = list(map(int, input().split()))

minimum = [-1] * n
maximum = [10**10] * n

l_max = 0
for i in range(n):
    if left_heights[i] > l_max:
        maximum[i] = left_heights[i]
        minimum[i] = left_heights[i]
    else:
        maximum[i] = left_heights[i]
        minimum[i] = 1
    l_max = left_heights[i]

r_max = 0
for i in reversed(range(n)):
    if right_heights[i] > r_max:
        if minimum[i] <= right_heights[i] <= maximum[i]:
            maximum[i] = right_heights[i]
            minimum[i] = right_heights[i]
        else:
            print(0)
            exit()
    else:
        if r_max >= minimum[i]:
            maximum[i] = min(right_heights[i], maximum[i])
            minimum[i] = max(1, minimum[i])  # 実は、この行は不要
        else:
            print(0)
            exit()

    r_max = right_heights[i]

mod = 10**9 + 7
ans = 1
for mi, ma in zip(minimum, maximum):
    ans *= ma - mi + 1
    ans %= mod
print(ans)
