n, w, k, v = list(map(int, input().split()))

col_val = [list(map(int, input().split())) for i in range(n)]

ans_list = []
ans_list += [j for i in range(8) for j in range(i+1) ]
ans_list += [i&7 for i in range(1000-72)]
ans_list += [j  for i in range(8) for j in range(i, 8)]

import random
import time

# 初期配置でのスコア計算

start = time.time()

scores = [[0 for _ in range(6)] for _ in range(125)]
# scores[i][j]は、下からi段目にj色から得られる得点
dan = [0 for _ in range(8)]
dan_block = [0 for _ in range(1000)]

for i in range(n):
    pos_yoko = ans_list[i]
    scores[dan[pos_yoko]][col_val[i][0]] += col_val[i][1]
    dan_block[i] = dan[pos_yoko]

    dan[pos_yoko] += 1

score_base = sum([max(row) for row in scores])


for rep in range(200000):
    x1 = random.randint(5, 990)
    x2 = x1 + 1

    # if swap(x1, x2)でスコアが上がるなら
    if x1 != x2:
        temp_1 = scores[dan_block[x1]].copy()
        temp_2 = scores[dan_block[x2]].copy()

        temp_1[col_val[x1][0]] -= col_val[x1][1]
        temp_2[col_val[x2][0]] -= col_val[x2][1]
        temp_1[col_val[x2][0]] += col_val[x2][1]
        temp_2[col_val[x1][0]] += col_val[x1][1]

        if max(temp_1) + max(temp_2) > max(scores[dan_block[x1]]) + max(scores[dan_block[x2]]):
            ans_list[x1], ans_list[x2] = ans_list[x2], ans_list[x1]
            scores[dan_block[x1]] = temp_1
            scores[dan_block[x2]] = temp_2


for i in ans_list:
    print(i) 

end = time.time()
# print(end - start)
# for i in range(8):
#     for j in range(i+1):
#         print(j)

# for i in range(1000 - 72):
#     print(i % 8)

# for i in range(8):
#     for j in range(i, 8):
#         print(j)
