import math

n = int(input())

coords = []
for i in range(n):
    x, y = list(map(int, input().split()))
    xy = [x, y]
    coords.append(xy)

ans_sq = 0
for i in range(n):
    for j in range(n):
        temp = (coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2
        if temp > ans_sq:
            ans_sq = temp

print(math.sqrt(ans_sq)) 
