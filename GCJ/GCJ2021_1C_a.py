# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00

# すでに買われたチケットによって、区間が分断されている
# ある区間に対して
### 1個買うと：通常は半分（偶奇考慮する必要あり）
###          端だと、全部
### 2個買うと：区間の上限と下限を買って区間を独占する
# 全探索してmaxを取る……までもないな。1個+1個の場合と2個の場合で貪欲して大きいほうだ。

n_test = int(input())
for i_test in range(n_test):

    n_pur, maxx = list(map(int, input().split()))
    purchased = list(map(int, input().split()))
    purchased.sort()

    ans = 0

    # 1個+1個
    interval = []
    for i in range(n_pur - 1):
        temp = (purchased[i+1] - purchased[i])//2
        interval.append(temp)

    # 両端
    interval.append(purchased[0] - 1)
    interval.append(maxx - purchased[-1])

    # 最も大きい区間2つ
    interval.sort()
    ans = interval[-1] + interval[-2]

    # 2個 このとき両端は選ばないものとして良い
    if n_pur >= 2:
        interval = []
        for i in range(n_pur - 1):
            temp = (purchased[i+1] - purchased[i]) - 1
            interval.append(temp)
        # 最も大きい区間1つ
        interval.sort()
        ans = max(ans, interval[-1])

    print("Case #{0}: {1}".format(i_test+1, ans/maxx))
