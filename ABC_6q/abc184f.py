# 半分全列挙
# N < 40 程度で「全ての場合のうち最も××なもの」だと半分全列挙を疑うのが良い
# ちなみに バレンタインデー は 18*2 = 36 で同じく半分全列挙。
# バレンタインデーのほうが、2つの集合に明示的に分けてあるから半分全列挙だと気づきやすいような、分けた後の方針を立てるのが難しいような。
# https://atcoder.jp/contests/abc018/tasks/abc018_4

n, t = list(map(int, input().split()))
nums = list(map(int, input().split()))

n_first = n // 2
n_second = n - n_first
first = nums[:n_first]
second = nums[n_first:]

first_time_all = [-1] * (1 << n_first)
second_time_all = [-1] * (1 << n_second)

for idx in range(1 << n_first):
    summ = 0
    for pos in range(n_first):
        if idx & (1 << pos):
            summ += first[pos]
    first_time_all[idx] = summ

for idx in range(1 << n_second):
    summ = 0
    for pos in range(n_second):
        if idx & (1 << pos):
            summ += second[pos]
    second_time_all[idx] = summ

first_time_all.sort()
second_time_all.sort()

idx_first = 0
idx_second = (1 << n_second) - 1
ans = 0
while True:
    if first_time_all[idx_first] + second_time_all[idx_second] > t:
        idx_second -= 1
        if idx_second < 0:
            break
    else:
        # 当該の組み合わせは条件を満たすので
        ans = max(ans, first_time_all[idx_first] + second_time_all[idx_second])
        idx_first += 1
        if idx_first >= (1 << n_first):
            break

print(ans)
