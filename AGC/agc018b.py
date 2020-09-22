# chokudaiブログの典型力の話を意識しつつ考えたら思いついた!

# 「ある集合の部分集合の中で、〜〜〜の値が最小になるものを求めよ」のパターン
# 愚直にやると2^Nを調べねばならず無理。
# したがって「一部を調べればよい」に帰着するのが多いだろう。
# 何らかの形でソートしておいて、空集合から1つずつ付け加えるとか。全体集合から1つずつ取り去るとか。

# 今回は全体集合から1つずつ取り去るのを考えるとできる。
# 全体集合である競技m0が最多の人数p0人を集めたとする。
# すると、全ての部分集合のうち「m0を含む集合」を考えると、競技m0は必ずp0人以上集まるので解もp0以上。
# ここで「m0を含む集合」について一気に計算できていることに注意! 一撃で多数の集合について計算が終わる。
# 次に全体集合からm0を取り去ったものを考える。
# ここである競技m1が最多の人数p1人を集めたとする。すると……以下同様。
# なお複数種目の競技が同率1位になった場合は全て一度に取り除いて良い。
# これで空集合までやって、最大が最小のものを出力すればOK! 

# 1744ms

n, m = list(map(int, input().split()))
preference = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)] # 1-index → 0-index

ans = n
held_sports = set(range(m))

while held_sports:
    # 各競技に参加する人数を求める
    parti = [0] * m
    for person in range(n):
        for s in range(m):
            if preference[person][s] in held_sports:
                parti[preference[person][s]] += 1
                break
    
    temp = max(parti)
    ans = min(ans, temp)
    # 集合から最大人数を取った要素を除外
    for idx, par in enumerate(parti):
        if par == temp:
            held_sports.remove(idx)

print(ans)