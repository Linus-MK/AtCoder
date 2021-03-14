import math
import random

def overlap(coords_0, coords_1):
    return ((not (coords_0[2] <= coords_1[0] or coords_1[2] <= coords_0[0])) and
    (not (coords_0[3] <= coords_1[1] or coords_1[3] <= coords_0[1])))

# サンプル 422343342 点

n = int(input())

xs = []
ys = []
rs = []
width_list = []

ans_list = [[0 for _ in range(4)] for _ in range(n)]
for i in range(n):
    x, y, r = list(map(int, input().split()))
    xs.append(x)
    ys.append(y)
    rs.append(r)

    # ans_list[i][0] = x
    # ans_list[i][1] = y
    # ans_list[i][2] = x+1
    # ans_list[i][3] = y+1

    width = int(math.sqrt(r*3//5))//2
    width_list.append(width)
    ans_list[i][0] = max(x-width, 0)
    ans_list[i][1] = max(y-width, 0)
    ans_list[i][2] = min(x+1+width, 10000)
    ans_list[i][3] = min(y+1+width, 10000)
    
for i in range(n):
    for j in range(i+1, n):
        count = 0
        while count <= 30:
            if overlap(ans_list[i], ans_list[j]):

                if random.random() < 0.5:
                    width = width_list[i]
                    width = width * 9 // 10
                    width_list[i] = width
                    ans_list[i][0] = max(xs[i]-width, 0)
                    ans_list[i][1] = max(ys[i]-width, 0)
                    ans_list[i][2] = min(xs[i]+1+width, 10000)
                    ans_list[i][3] = min(ys[i]+1+width, 10000)
                else:
                    width = width_list[j]
                    width = width * 9 // 10
                    width_list[j] = width
                    ans_list[j][0] = max(xs[j]-width, 0)
                    ans_list[j][1] = max(ys[j]-width, 0)
                    ans_list[j][2] = min(xs[j]+1+width, 10000)
                    ans_list[j][3] = min(ys[j]+1+width, 10000)
            
            else:
                break
        
        if overlap(ans_list[i], ans_list[j]):
            # 少しずつ縮めていってもまだ重なってるようなら、強制的に縦横1にします
            ans_list[i][0] = xs[i]
            ans_list[i][1] = ys[i]
            ans_list[i][2] = xs[i]+1
            ans_list[i][3] = ys[i]+1
 
            ans_list[j][0] = xs[j]
            ans_list[j][1] = ys[j]
            ans_list[j][2] = xs[j]+1
            ans_list[j][3] = ys[j]+1

for i in range(n):
    print(f'{ans_list[i][0]} {ans_list[i][1]} {ans_list[i][2]} {ans_list[i][3]}')

