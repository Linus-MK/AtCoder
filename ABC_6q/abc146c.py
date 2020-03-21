a, b, x = list(map(int, input().split()))

ans = 0
# 10**9を買える場合
if x >= a * (10**9) + b * 10:
    print(10**9)
    exit()

for i in range(1, 10):
    max_num_afford = (x - (b * i)) // a
    max_num = 10 ** i - 1
    max_num_afford = min(max_num_afford, max_num)
    min_num = 10 ** (i-1)

    if max_num_afford >= min_num:
        ans = max_num_afford

print(ans)
