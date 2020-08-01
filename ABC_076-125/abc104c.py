# 方針〜
# Dが10以下なのがポイント
# 全ての部分集合に対して「この集合を全問解いた場合、総合スコアをG点以上にするために何問解くか」をビット全探索すれば良い。
# Dividing Chocolate (ABC159-E)と似たようなもの

# なお、「この集合を全問解いた場合、総合スコアをG点以上にするために何問解くか」を解くときには
# 得点の高い方からGreedyだが、途中でコンプリートした時のボーナスを無視しても正しい答えは出せる。
# それ自体のスコアは間違いになるが、問題数が増える方向に間違うし、正しい部分集合のときには正しい問題数が得られるので。
# 今回は上記の方法でやってみる。

d, goal = list(map(int, input().split()))
problems = [list(map(int, input().split())) for _ in range(d)]

ans = 10 ** 6 * 10 * 2
for completed in range(2 ** d):
    
    point_all = 0
    num_problem = 0

    # 最下位のdigitが100点問題
    for point in range(d):
        if (completed & 2 ** point) > 0:
            point_all += 100 * (point+1) * problems[point][0]
            point_all += problems[point][1]
            num_problem += problems[point][0]
    
    if point_all < goal:
        for point in reversed(range(d)):
            if (completed & 2 ** point) == 0:
                p = (100 * (point+1))
                n = (goal - point_all + p - 1) // p
                n = min(problems[point][0], n)

                point_all += n * p  # ボーナス点は無視する
                num_problem += n

                if point_all >= goal:
                    break

    # 目標点数を達成しているとは限らないことに注意 条件に目標達成を入れる
    if point_all >= goal and num_problem < ans:
        ans = num_problem

print(ans)
