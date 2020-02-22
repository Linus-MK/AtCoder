n = int(input())
coord = list(map(int, input().split()))

ans = 10 ** 9
for kaisai in range(100 + 1):
    tairyoku = 0
    for c in coord:
        tairyoku += (c - kaisai) ** 2
    ans = min(ans, tairyoku)

print(ans)
