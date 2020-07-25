n = int(input())
nums = list(map(int, input().split()))

num_free = 0
num_color = [False] * 8
for rate in nums:
    if rate < 3200:
        num_color[rate // 400] = True
    else:
        num_free += 1

ans = sum(num_color)
print('{} {}'.format(max(ans, 1), ans + num_free))
