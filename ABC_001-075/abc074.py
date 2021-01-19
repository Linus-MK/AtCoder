# 解説とぜんぜん違う考え方で解いたっぽい。後で考え方をまとめておこう。

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

dist_sum = sum([sum(line) for line in dist])
dist_sum //= 2

feasible = True
for start in range(n):
    for end in range(start, n):
        for mid in range(n):
            if start == mid or end == mid:
                continue
            if dist[start-1][mid-1] + dist[mid-1][end-1] < dist[start-1][end-1]:
                feasible = False
                break
            if dist[start-1][mid-1] + dist[mid-1][end-1] == dist[start-1][end-1]:
                dist_sum -= dist[start-1][end-1]
                break

if not feasible:
    print(-1)
else:
    print(dist_sum)
