# 座標の変換。
# (0,0)(1,0)(0,1)の3点の移動先を計算すれば良い。

n = int(input())
coords = [list(map(int, input().split())) for i in range(n)]

m = int(input())
operations = [list(map(int, input().split())) for i in range(m)]

q = int(input())
queries = [list(map(int, input().split())) for i in range(q)]

origin = [[0 for _ in range(2)] for _ in range(m+1)]
origin[0][0] = 0
origin[0][1] = 0
x_one = [[0 for _ in range(2)] for _ in range(m+1)]
x_one[0][0] = 1
x_one[0][1] = 0
y_one = [[0 for _ in range(2)] for _ in range(m+1)]
y_one[0][0] = 0
y_one[0][1] = 1

for ope_i in range(m):
    ope = operations[ope_i]
    
    if ope[0] == 1:
        origin[ope_i+1][0] =  origin[ope_i][1]
        origin[ope_i+1][1] = -origin[ope_i][0]
        x_one[ope_i+1][0] =  x_one[ope_i][1]
        x_one[ope_i+1][1] = -x_one[ope_i][0]
        y_one[ope_i+1][0] =  y_one[ope_i][1]
        y_one[ope_i+1][1] = -y_one[ope_i][0]
    elif ope[0] == 2:
        origin[ope_i+1][0] = -origin[ope_i][1]
        origin[ope_i+1][1] =  origin[ope_i][0]
        x_one[ope_i+1][0] = -x_one[ope_i][1]
        x_one[ope_i+1][1] =  x_one[ope_i][0]
        y_one[ope_i+1][0] = -y_one[ope_i][1]
        y_one[ope_i+1][1] =  y_one[ope_i][0]
    elif ope[0] == 3:
        p = ope[1]
        origin[ope_i+1][0] = 2*p - origin[ope_i][0]
        origin[ope_i+1][1] =  origin[ope_i][1]
        x_one[ope_i+1][0] = 2*p - x_one[ope_i][0]
        x_one[ope_i+1][1] =  x_one[ope_i][1]
        y_one[ope_i+1][0] = 2*p - y_one[ope_i][0]
        y_one[ope_i+1][1] =  y_one[ope_i][1]
    elif ope[0] == 4:
        p = ope[1]
        origin[ope_i+1][0] =  origin[ope_i][0]
        origin[ope_i+1][1] = 2*p - origin[ope_i][1]
        x_one[ope_i+1][0] =  x_one[ope_i][0]
        x_one[ope_i+1][1] = 2*p - x_one[ope_i][1]
        y_one[ope_i+1][0] =  y_one[ope_i][0]
        y_one[ope_i+1][1] = 2*p - y_one[ope_i][1]

for q in queries:
    phase = q[0]

    x = origin[phase][0] + (x_one[phase][0] - origin[phase][0]) * coords[q[1]-1][0] + (y_one[phase][0] - origin[phase][0]) * coords[q[1]-1][1]
    y = origin[phase][1] + (x_one[phase][1] - origin[phase][1]) * coords[q[1]-1][0] + (y_one[phase][1] - origin[phase][1]) * coords[q[1]-1][1]
    print(f'{x} {y}')

