# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

# テストセット1 ビット全探索しろ。
# テストセット2
# CJの切り替えに対してコストが発生するので、切り替えないほうが良い。
# C???Cだったら間を全部Cで埋めたほうが良いに決まっている。J???Jも同じ。
# 両端がCとJの場合は、間をどちらか一方で全部埋めると、1回だけ切り替えのコストが発生する。
# 結局、?を全部無視（削除）してコストを求めればよい。


N = int(input())
for i_test in range(N):

    sp = input().split()
    cost_cj = int(sp[0])
    cost_jc = int(sp[1])
    sentense = sp[2]

    sentense = sentense.replace('?', '')
    if len(sentense) < 2:
        ans = 0
    else:
        ans = 0
        for i in range(len(sentense) - 1):
            if sentense[i] == 'C' and sentense[i+1] == 'J':
                ans += cost_cj
            elif sentense[i] == 'J' and sentense[i+1] == 'C':
                ans += cost_jc

    print("Case #{0}: {1}".format(i_test+1, ans))
