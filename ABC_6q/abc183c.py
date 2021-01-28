# 全探索 ただしbitではなく順列の全探索

import itertools

n, dist_target = list(map(int, input().split()))

dist_matrix = []
for i in range(n):
    dist_matrix.append(list(map(int, input().split())))

ans = 0
for perm in itertools.permutations(range(1, n)):
    perm = [0] + list(perm) + [0]
    dist = 0
    for i in range(n):
        dist += dist_matrix[perm[i]][perm[i+1]]
    if dist == dist_target:
        ans += 1

print(ans)
