# 以下の貪欲法は嘘解法（通るらしい）。
# 「高橋くんは右方向に落とすように、なるべく右を選ぶ。青木くんは落ちない範囲で左を選ぶ。これで落ちるか落ちないか判定する。
# これを上下左右で繰り返し、落ちなければ」
# 盤面が縦が十分大きい×横3、初期位置が中央、
# UULLRR
# RLUUUU
# は正解NOだが、貪欲でYESになってしまう。

# https://www.youtube.com/watch?v=Rr5ul_LDMiw
# コメントより：
# 3×3中央で、
# DRLL
# RUDD
# 初手青木くんがRなら高橋くんはそのままRするし、でなければLLしてどのみち外に出せる。

h, w, n = list(map(int, input().split()))
row, column = list(map(int, input().split()))
s_sente = input()
s_gote = input()

ans = [0, h-1, 0, w-1]
for i in reversed(range(n)):
    g = s_gote[i]
    if g == 'U':
        ans[1] = min(ans[1] + 1, h-1)
    elif g == 'D':
        ans[0] = max(ans[0] - 1, 0)
    elif g == 'L':
        ans[3] = min(ans[3] + 1, w-1)
    elif g == 'R':
        ans[2] = max(ans[2] - 1, 0)
    # print(ans)

    # ここはmax/minを取ってはいけない。0〜h-1 or w-1までの範囲から出ることもあるし、下のif notの判定条件のためにはそれが必要。
    s = s_sente[i]
    if s == 'U':
        ans[0] = ans[0] + 1
    elif s == 'D':
        ans[1] = ans[1] - 1
    elif s == 'L':
        ans[2] = ans[2] + 1
    elif s == 'R':
        ans[3] = ans[3] - 1
    
    if not (ans[0] <= ans[1] and ans[2] <= ans[3]):
        print('NO')
        exit()
    # print(ans)

if ans[0] <= row-1 <= ans[1] and ans[2] <= column-1 <= ans[3]:
    # 「最後までコマが残るような初期配置の範囲」に、所与の初期配置が含まれる
    print('YES')
else:
    print('NO')
