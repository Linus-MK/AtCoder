# 美しさの定義：累積和。前処理をO(N)で行っておけば、それぞれの部分和はO(1)で計算可能。
# N <= 1000なので、部分和の数 <= 500000。
# 決め打ち二分探索かなぁ。
# ビットごとの操作で最大値→上位ビットから確定して良い。

# 上位ビットから順に
#     当該のビットを1にできますか?
#     これは、1になっているビットがK個以上あるかで決められる……ってこれ真面目にやったらO(部分和の数) かかるじゃん。
#     1にするなら条件を満たさない部分は使用できないので除外

# 貪欲法か? 大きい値k個のbit andが答えだったりする?
# →NO 大きい値k個だと32が立つけど16も8も立たない。だけど全体を見れば32+8のビットがk個以上存在する、みたいな場合は多分作れそうだ。

# 答えとしてありうる数で一番大きいのは?
# N - 1000, a_i = 10**9, k = 2だと 10**9*999が最高。ざっと10**12 < 2 ** 40である。
# 500000 * 36 = 18000000 = 1800万か。これで良いんだろう、うん。
# →Python3でもPyPyでも余裕で通った。1800万にしては意外と速いな。

n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

cumsum = [0] * (n+1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + nums[i]

interval_sum = [0] * (n * (n+1) // 2)
idx = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        interval_sum[idx] = cumsum[j] - cumsum[i]
        idx += 1 

interval_sum.sort(reverse=True)
# print(interval_sum)

# 全てのケースで 2^39 のビットからやっても良いけど。 最上位ビットを出しておこう。
bit_len = len(format(interval_sum[0], 'b'))  # 2進数表記したときの文字列の長さ

ans = 0
for idx in reversed(range(bit_len)):
    filtered = [num for num in interval_sum if (num & (1 << idx))]
    if len(filtered) >= k:
        ans |= (1 << idx)
        interval_sum = filtered
    else:
        pass

print(ans)
