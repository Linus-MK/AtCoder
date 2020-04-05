# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9?show=progress

N = int(input())
for i in range(N):
    num = int(input())
    schedules = [list(map(int, input().split())) + [j] for j in range(num)]
    
    schedules.sort(key=lambda x: x[0])

    j_end_time = -1  # 現在のタスクが終了する時刻
    c_end_time = -1
    ans = [''] * num

    for sche in schedules:
        start = sche[0]
        end = sche[1]
        idx = sche[2]
        if j_end_time <= start:
            j_end_time = end
            ans[idx] = 'J'
        elif c_end_time <= start:
            c_end_time = end
            ans[idx] = 'C'
        else:
            # IMPOSSIBLE
            ans = 'IMPOSSIBLE'
            break
    
    if ans != 'IMPOSSIBLE':
        ans = ''.join(ans)

    print("Case #{0}: {1}".format(i+1, ans))
