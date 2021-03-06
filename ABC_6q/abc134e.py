# 貪欲でいいよね。
# 最初から順に見ていって、増加列で取れるならそのうち最大のもので取る、無理なら新設する。
# これが最適な理由は……厳密には難しいなぁ。ちゃんと分かってない。

# でこれを実現するデータ構造は何が良いかを考えるわけよね。
# ソートしたデータから指定のものを探す・値を取り出す・新規で入れる をしなきゃいけないから、C++のset（平衡二分探索木）使わないと無理じゃね?
# と一瞬思うけど、普通のリストで可能。
# なぜなら、値を書き換えることでソートは崩れないから。
# Tが来たら、T未満のうち最も右の要素を見つけて、Tに書き換える。T未満とT以上の境界なので、Tに書き換えても値はソート順を飛び越さない。

# 昇順で管理だとTLEなので降順にします→bisectが使えないやんけ→-1倍して昇順にします

import bisect

n = int(input())

ans = 0
mylist = []
for i in range(n):
    k = int(input())
    idx = bisect.bisect(mylist, -k)
    if idx == ans:
        mylist.append(-k)
        ans += 1
    else:
        mylist[idx] = -k  # この操作によりソートは崩れない

print(ans)
