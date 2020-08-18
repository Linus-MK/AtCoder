n, m = list(map(int, input().split()))
condition = [list(map(int, input().split())) for _ in range(m)]

condition.sort(key=lambda a: (a[1], a[0]))

right_end = 0
ans = 0
for c in condition:
    if c[0] >= right_end:
        ans += 1
        right_end = c[1]
print(ans)

# 「各タスクの開始時刻と終了時刻が与えられて、タスクを最大いくつ実行できるか（区間スケジューリング問題）」の問題の答えと同じ（証明はできていない）
# →終了時刻の順番にソートして、やれるならやる（貪欲）。（蟻本 p.43）

# 解説動画 https://www.youtube.com/watch?v=nVSWen0oM38 ：
# 区間の右側でソートする。右側が最小のものを取る。この右端よりも左側で一本必ず落とさねばならない。すぐ左の橋を落とすのが最適。（それよりも左だと損をする。）
# まだ通行可能な区間のうち、右側が最小のものを取る。この右端よりも左で一本必ず落とさねばならない。以下同じ。
