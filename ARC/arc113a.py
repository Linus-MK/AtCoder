# どうするのが良かったんだ……?
# 何も考えない全探索だと、探索範囲が 1 <= a, b, c <= KなのでO(K^3)となり、死ぬ。
# a, b を固定すれば、cは最大値を求めるだけなので定数時間で求まるが、それだとO(K^2)となり、死ぬ。
# いや、bの早期breakを入れれば間に合うか? 
# 間に合うな。計算時間O(KlogK)だな。

# a <= b <= c となる組み合わせだけ数えて、組み合わせに応じて入れ替えを含めて何通りあるか数えた。
# cは愚直に最小値bから全部調べた。大小関係がどうなるか（何通りになるか）分からなかったので。
# 制限時間が2秒に対して1.5秒程度かかってるので、ちょっと危なかった。

n = int(input())

ans = 0
for a in range(1, n+1):
    for b in range(a, n+1):
        ab = a * b
        if ab > n:
            break
        for c in range(b, n+1):
            abc = ab * c
            if abc > n:
                break
            if a==b==c:
                ans += 1
            elif a==b or b==c:
                ans += 3
            else:
                ans += 6

print(ans)
