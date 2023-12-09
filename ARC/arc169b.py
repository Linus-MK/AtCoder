# これもグラフやんけ
# 切るポイント→次に切るポイントのグラフを作る

n, sum_limit = list(map(int, input().split()))
nums = list(map(int, input().split()))

# 切るポイント→次に切るポイントのグラフを作る
# 累積和と二分探索

num_accum = [0] * (n+1)
for i in range(n):
    num_accum[i] = num_accum[i-1] + nums[i]

num_accum[n] = num_accum[n-1] + 10 ** 18  # 番兵
num_accum = [0] + num_accum
# print(num_accum)

# cut_next[i] = j は
# 最初に要素i-1とiの間で切ったら、次は要素j-1とjの間で切る、ことを示す。
# nums[0]より前で切るケースを考える必要あることに注意。

cut_next = [-1] * (n)

def is_valid(mid, i):
    return num_accum[mid] - num_accum[i] > sum_limit


for i in range(n):
    
    cut_ok = n+1
    cut_ng = i

    # めぐる式二分探索
    while abs(cut_ok - cut_ng) > 1:
        mid = (cut_ok + cut_ng) // 2
        # print(mid, i, num_accum[mid] - num_accum[i])
        if is_valid(mid, i):
            cut_ok = mid
        else:
            cut_ng = mid

    # print(cut_ng)
    cut_next[i] = cut_ng

# print(cut_next)

valid_interval = [0] * (n+1)  # その切れ目を含むような l, rの通り数
valid_left = [0] * (n+1)  # その切れ目を含むような lの通り数

for i in range(n-1):
    valid_left[cut_next[i]] += valid_left[i] + 1

for i in range(n):
    valid_interval[i] = valid_left[i] * (n-i)

# print(valid_left)
# print(valid_interval)

print(sum(valid_interval) + (n+1) * n // 2)