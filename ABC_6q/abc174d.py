# 終了状態はRR...WW...となる。
# 終了状態を1つ固定したら、そこまでの回数は単純な計算で求まるので、
# 終了状態を順次変えながら全通り試して最小値を取れば良い

n = int(input())
stones = input()

t = stones.count('R')

num_not_equal = t
red_num_diff = t
red_count = 0

ans = t
for s in stones:
    if s == 'R':
        num_not_equal -= 1
    else:
        num_not_equal += 1

    red_count += 1
    red_num_diff = abs(red_count - t)

    temp = red_num_diff + (num_not_equal - red_num_diff) // 2
    ans = min(ans, temp)

    # print(num_not_equal, red_num_diff)

print(ans)

