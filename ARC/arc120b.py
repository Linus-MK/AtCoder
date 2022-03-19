mod = 998244353
h, w = list(map(int, input().split()))
masu = []
for i in range(h):
    masu.append(input())

# O(hw) で計算量に余裕がありそうなので、効率悪目の書き方でも通るだろ。

ans = 1
for line_idx in range(0, h+w-2+1):
    appeared = set()
    for row in range(h):
        col = line_idx - row
        if not (0 <= col < w):
            continue
        color = masu[row][col]
        if color != '.':
            appeared.add(color)
    ans *= (2 - len(appeared))
    ans %= mod

print(ans)
