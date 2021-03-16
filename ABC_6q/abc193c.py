n = int(input())

# 少ないnでバグりそうだから特別扱い
if n <= 3:
    print(n)
    exit()

# 一つ一つ「表せるか否か」を調べていると間に合わない
# 表せるやつが少なそうだから、数え上げて全体から引けば良い
# 重複に注意

ans_set = set()
for base in range(2, n):
    if base * base > n:
        break
    for power in range(2, 50+1):
        if base**power > n:
            break
        ans_set.add(base**power)

print(n - len(ans_set))
