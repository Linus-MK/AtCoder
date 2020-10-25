# 横方向（w）<=8なので、ある1行の横棒の入り方は全部リストアップできる。
# 明らかな上界は2^(8-1)=128で、実際にはもっと少ないはず!
# ただこれを100回つなげるのを愚直にやるとTLEするので、
# dp[row][dest] := row段目からなるあみだくじで、到達点がdestであるようなあみだくじの個数
# として動的計画法をすればよい。

h, w, k = list(map(int, input().split()))

if w == 1:
    # kは必ず1になる。
    print(1)
    exit()

all_perm = []

for idx in range(2**(w-1)):
    valid = True
    has_bar = False
    for digit in range(w-1):
        if (idx & (2 ** digit)):
            if has_bar == True:
                valid = False
                break  # invalid
            has_bar = True
        else:
            has_bar = False
    
    if valid:
        # print(bin(idx))

        perm = list(range(w))
        for digit in range(w-1):
            if (idx & (2 ** digit)):
                perm[digit] = digit+1
                perm[digit+1] = digit
        
        all_perm.append(perm)
    
# dp[row][dest] := row段目からなるあみだくじで、到達点がdestであるようなあみだくじの個数

dp = [[0 for _ in range(w)] for _ in range(h+1)]
dp[0][0] = 1

# 集めるDPだと書きづらい気がする。配るDPの方で。
mod = 10 ** 9 + 7
for row in range(h):
    for dest in range(w):
        dp[row][dest] %= mod
        for perm in all_perm:
            # もちろんここは高速化可能で、destからdest_nextが1つ右/そのまま/1つ左のどれになるタイプがいくつあるかを最初に数え上げれば良い。
            # が、今回はそこまで必要ない
            dest_next = perm[dest]
            dp[row+1][dest_next] += dp[row][dest]

print(dp[-1][k-1] % mod)
