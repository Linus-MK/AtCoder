n = int(input())
nums = list(map(int, input().split()))
mod = 10 ** 9+7
# 左から順に処理する。10**(桁数)倍をしてその数を足して、modで割る
ans = 0
for i in nums:
    ans *= 10 ** (len(str(i)))
    ans += i
    ans %= mod
print(ans)
