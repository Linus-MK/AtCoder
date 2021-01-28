# kyopro_friendsさんが言ってた覚えがある! 直前の同じものだけ見ればあとは忘れても良いってパターンだ!
#  https://twitter.com/kyopro_friends/status/1289921719444967426 ABC174 F問題 Range Set Query

# あとABC179 F問題も同種のテクニック使ってる? これもリバーシだな。
#  https://twitter.com/kyopro_friends/status/1307315732812713986

# 1次元DP、各色について、最も右側の同色の石の位置を覚えておく、
# 右に1個追加したときに「その石をを使って裏返すか、裏返さないか」で場合分けして足し算。

n = int(input())
colors = [int(input()) for _ in range(n)]
last_pos = {}

dp = [0] * n
dp[0] = 1
last_pos[colors[0]] = 0
mod = 10 ** 9 + 7 
for i in range(1, n):
    last = last_pos.get(colors[i])
    if last != None and last < i-1:
        dp[i] = (dp[i-1] + dp[last]) % mod
    else:
        dp[i] = dp[i-1]
    last_pos[colors[i]] = i

print(dp[n-1])
