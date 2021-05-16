# AtCoder 徒競走 の類似問題。
# コードコピペして一部書き換えた。
# n! を全列挙すると間に合わない。
# bit DPで解く。
# 「徒競走」では明示されていた前後関係が、この問題では暗黙的になっているので、前後関係を構成すればよい。

import sys
input = sys.stdin.readline

N = int(input())
for i_test in range(N):

    n = int(input())
    if n > 13:
        exit()
    
    visibles = list(map(int, input().split()))

    # condition = [list(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
    # 1-index→0-index

    # このconditionさえ作れればOK

    # 異常系をチェック
    valid = True
    if visibles[0] != 1:
        valid = False
    for i in range(n-1):
        if visibles[i+1] - visibles[i] > 1:
            valid = False
    if not valid:
        print("Case #{0}: {1}".format(i_test+1, 0))
        continue

    condition = []
    visible_idx = [0]
    for idx in range(1, n):
        if visibles[idx] == visibles[idx-1] + 1:
            for v in visible_idx:
                condition.append([v, idx])
            visible_idx.append(idx)
        else:
            # 見えなくなったやつがある
            t = visibles[idx] - 1
            for v in visible_idx[:t]:
                condition.append([v, idx])
            for v in visible_idx[t:]:
                condition.append([idx, v])
            visible_idx = visible_idx[:t]
            visible_idx.append(idx)
    
    # print(condition)

    dp = [0] * (2**n)
    dp[0] = 1 # 空集合をトポロジカルソートする場合の数
    for idx in range(1, 2**n):
        # 先に各digitが1位になる可能性があるか否かをまとめて計算する
        may_be_first = [True] * n
        digit_set = {digit for digit in range(n) if 1<<digit & idx}
        for pair in condition:
            # S-v がfitst, vがsecondとなる対があるか
            if pair[0] in digit_set and pair[1] in digit_set:
                may_be_first[pair[1]] = False

        for digit in range(n):
            if digit in digit_set:  # digitに対応する頂点vが、今考えている頂点集合Sに含まれていて
                if may_be_first[digit]:
                    dp[idx] += dp[idx - (1<<digit)]

    # print(dp[-1])
    # print(dp)

    print("Case #{0}: {1}".format(i_test+1, dp[-1]))