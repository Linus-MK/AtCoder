# 今回は座標圧縮は不要である 解説にも書いてある： https://www.slideshare.net/chokudai/abc014

n = int(input())

enquate = [list(map(int, input().split())) for _ in range(n)]

x = [0] * 1000002

for interval in enquate:
    start = interval[0]
    x[start] += 1

    end = interval[1]
    x[end+1] -= 1

ans = 0
now = 0
for diff in x:
    now += diff
    ans = max(ans, now)

print(ans)
