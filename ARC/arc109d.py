n_test = int(input())
for _ in range(n_test):
    x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))

    x_min = min(x1, x2, x3)
    y_min = min(y1, y2, y3)
    coord_set = {(x1, y1), (x2, y2), (x3, y3)}
    # 向き特定
    if (x_min, y_min) not in coord_set:
        direction = 'right-up'
    elif (x_min, y_min+1) not in coord_set:
        direction = 'left-up'
    elif (x_min+1, y_min) not in coord_set:
        direction = 'right-down'
    elif (x_min+1, y_min+1) not in coord_set:
        direction = 'left-down'
    
    if (x_min <= 0 and y_min >= 0) or (x_min >= 0 and y_min <= 0):
        base = max(abs(x_min), abs(y_min))
        print(base*2)
    else:
        base = max(abs(x_min), abs(y_min))
        print(base*2)

