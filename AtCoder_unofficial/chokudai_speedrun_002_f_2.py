# setに入れてしまってその長さとかで解けないかな?
# setやlistはsetに入れられない。
# 1つの数に置き換えれば良い 大*10**10 + 小 なら

# Python (3.8.2)で462ms

n = int(input())
ans = set()
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a < b:
        a, b = b, a
    # どちらを使ってもほぼ同じ速度だった。ビットシフトのほうが速そうだけど。
    ans.add(a*10**10 + b)
    # ans.add((a<<30) + b)
print(len(ans))
