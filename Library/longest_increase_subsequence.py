# 現状、chokudai speedrun 001 h問題の解答コードそのまんま。
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_h

# 最長増加部分列
# Longest Increase Subsequence
# ABC006−解説 https://www.slideshare.net/chokudai/abc006
# いかたこのたこつぼ https://ikatakos.com/pot/programming_algorithm/dynamic_programming/longest_common_subsequence

# 動的計画法と二分探索を使ってO(NlogN)で求められる

from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
inf = 10**10

dp = [inf] * (n + 1)
# dp[j] を、A1〜Aiまでで長さjの増加部分列が作れるならばその最後の要素の最小値、
# 作れないならばinfとする(0-indexed)
dp[0] = -inf  # atcoderのslideshareがそうやってた。単調増加性を確保するための番兵だろう

for i in range(n):
    # ここで書き換える必要があるのは1つの要素だけ。
    # p >= nums[i]を満たす最小のpである。
    # 単調性より、二分探索で該当要素を求める
    pos = bisect_left(dp, nums[i])
    dp[pos] = nums[i]

# 最後に、dp[k] < infとなる最大のkを求める
ans = bisect_left(dp, inf) - 1
print(ans)
