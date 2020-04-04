import math

n = int(input())

coords = [list(map(int, input().split())) for j in range(n)]

distance_sum = 0
for i in range(n):
    for j in range(i+1, n):
        distance_sum += math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

print(distance_sum * (n-1) / (n * (n-1) // 2) )
# 完全グラフの変数は n * (n-1) // 2, うち1回の経路で使うのはn-1本。
# 約分して以下のようにもできる；
# print(distance_sum * 2 / n)
