# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01

def concat(start, n_concat):
    ans = ''
    for i in range(n_concat):
        ans += str(start + i)
    return int(ans)

n_test = int(input())
for i_test in range(n_test):

    num = int(input())

    if num < 12:
        ans = 12
    else:
        ans = num * 100
        # いくつの数をくっつけるか、で全探索 
        str_num = str(num)
        length = len(str_num)
        # numが例えば9955のときは答えは12345、n_concatは5 つまりn_concat はlength+1になる可能性もある
        for n_concat in range(2, length + 1 + 1):
            # n_concat 個の数をくっつける。このとき、開始の数が大きければ、つなげた結果できる数も大きい。（単調増加性がある。）
            # あっこれ二分探索で正解を探せるやつじゃないか?
            # めぐる式二分探索
            ok = 10 ** 10
            ng = 0 # 1はOKになる可能性があるので0

            while abs(ok-ng) > 1:
                mid = (ok + ng) // 2

                # print(ok, ng)

                temp = concat(mid, n_concat)
                if(temp > num):
                    ok = mid
                else:
                    ng = mid
            
            ans_temp = concat(ok, n_concat)
            ans = min(ans_temp, ans)

    print("Case #{0}: {1}".format(i_test+1, ans))
