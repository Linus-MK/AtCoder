# 用語をここで整理しておこう
# 順序関係が整合しているので、有向グラフに書き直すとそのグラフはDAG（）になります（蟻本p.89）
# トポロジカル順序、トポロジカルソートの問題（蟻本p.89-90）
# 解法はbitDP（蟻本p.173）
# 蟻本にある巡回セールスマン問題、今回の徒競走とも、bitDPでメモ化してN!の計算量を2^Nに落とす問題

# 疑問：例えば1と2に直接関係がないけど1-3-2の順序が決まっている場合、集合(1,2)で実際にありえない順序(2-1)をカウントしてしまわないか?
# 解答：問題ない。集合(1,2,3)の数を考えるときに、集合(1,2)のカウントは（3が先頭に来ないから）合計されないので、最終的な結果に影響しない。

# PyPy3だと通る（マジかよ）
# 計算量は外側のループから順に、2**n * (n + m)
# 2**16 * (16 + (16*15)/ 2) = 8912896
# PyPy3 169ms
# Python 1626ms(この問題は制約3sec)

import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))

condition = [list(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
# 1-index→0-index

dp = [0] * (2**n)
dp[0] = 1 # 空集合をトポロジカルソートする場合の数
for idx in range(1, 2**n):
    # 先に各digitが1位になる可能性があるか否かをまとめて計算する
    may_be_first = [True] * n
    for pair in condition:
        # S-v がfitst, vがsecondとなる対があるか
        if (1<<pair[0] & idx) and (1<<pair[1] & idx):
            may_be_first[pair[1]] = False

    for digit in range(n):
        if 1<<digit & idx:  # digitに対応する頂点vが、今考えている頂点集合Sに含まれていて
            if may_be_first[digit]:
                dp[idx] += dp[idx - (1<<digit)]

print(dp[-1])
# print(dp)