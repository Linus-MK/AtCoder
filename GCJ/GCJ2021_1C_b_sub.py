# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01

import bisect

def concat(start, n_concat):
    ans = ''
    for i in range(n_concat):
        ans += str(start + i)
    return int(ans)

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

n_test = int(input())

roaring_list = []
for n_concat in range(2, 7+1):
    for start in range(1, 10000):
        roaring = concat(start, n_concat)
        if roaring <= 10**6:
            roaring_list.append(roaring)
        else:
            break
roaring_list.append(1234567) # 10**6以上最小 たぶん
roaring_list.sort()

for i_test in range(n_test):

    num = int(input())
    ans = find_gt(roaring_list, num)

    # if num < 12:
    #     ans = 12
    # else:
    #     ans = num * 100
    #     # いくつの数をくっつけるか、で全探索 
    #     str_num = str(num)
    #     length = len(str_num)
    #     for n_concat in range(2, length + 1):
    #         # n_concat 個の数をくっつける。このとき、開始の数が大きければ、つなげた結果できる数も大きい。（単調増加性がある。）
    #         # あっこれ二分探索で正解を探せるやつじゃないか?
    #         # めぐる式二分探索
    #         ok = 10 ** 10
    #         ng = 0 # 1はOKになる可能性があるので0

    #         while abs(ok-ng) > 1:
    #             mid = (ok + ng) // 2

    #             # print(ok, ng)

    #             temp = concat(mid, n_concat)
    #             if(temp > num):
    #                 ok = mid
    #             else:
    #                 ng = mid
            
    #         ans_temp = concat(ok, n_concat)
    #         ans = min(ans_temp, ans)

    print("Case #{0}: {1}".format(i_test+1, ans))
