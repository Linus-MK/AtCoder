n, m = list(map(int, input().split()))

condition = []
for i in range(m):
    condition.append(list(map(int, input().split())))
k = int(input())

put_ball = []
for i in range(k):
    put_ball.append(list(map(int, input().split())))

ans = 0
for set_idx in range(1 << k):
    num_balls = [0] * (n + 1)
    for bit in range(k):
        if set_idx & (1<<bit):
            j = put_ball[bit][0]
        else:
            j = put_ball[bit][1]
        num_balls[j] += 1
    # print(num_balls)
    valid = 0
    for con in condition:
        if num_balls[con[0]] >= 1 and num_balls[con[1]] >= 1:
            valid += 1
    ans = max(ans, valid)

print(ans)
