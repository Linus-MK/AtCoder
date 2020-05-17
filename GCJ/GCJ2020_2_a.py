# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9?show=progress

import math

N = int(input())
for ix in range(N):
    left, right = list(map(int, input().split()))
    
    # one_side = ある人数までは片方から取り続ける。その人数 one_side を求める
    if left == right:
        one_side = 0
    else:
        dif = abs(left - right)
        temp = int(math.sqrt(dif * 2)) - 1
        while (True):
            if (temp + 1) * temp // 2 >= dif:
                break
            else:
                temp += 1
        one_side = temp
    
    # print(one_side)

    if left > right :
        left -= one_side * (one_side + 1) // 2
    else:
        right -= one_side * (one_side + 1) // 2

    # これ以降は左右交互にとっていくことになる。
    # ok の値が、「取り切れない最小の個数」になるようにしたい
    # めぐる式二分探索
    ok = 10 ** 10
    ng = -1

    while abs(ok-ng) > 1:
        mid = (ok + ng) // 2

        # print(ok, ng)

        amount = ((one_side + 1) + (one_side + 1 + 2 * (mid-1))) * mid // 2
        if(amount > max(left, right)):
            ok = mid
        else:
            ng = mid
    
    mid = ng
    swap = False
    if right > left:
        swap = True
        left, right = right, left
    
    left -= ((one_side + 1) + (one_side + 1 + 2 * (mid-1))) * mid // 2
    right -= ((one_side + 2) + (one_side + 2 + 2 * (mid-1))) * mid // 2
    # 最後を取り去れるどうかで分岐

    if right < 0:
        right += one_side + 2 + 2 * (mid-1)
        k = one_side + 1 + 2 * (mid-1)
    else:
        k = one_side + 2 + 2 * (mid-1)

    if swap: 
        print("Case #{0}: {1} {2} {3}".format(ix+1, k, right, left))
    else:
        print("Case #{0}: {1} {2} {3}".format(ix+1, k, left, right))
