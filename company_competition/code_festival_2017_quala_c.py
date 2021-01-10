h, w = list(map(int, input().split()))

masu = []
for i in range(h):
    masu.append(input())

# それぞれの文字が何回あるかカウント
count = [0] * 26
for line in masu:
    for ch in line:
        idx = ord(ch) - ord('a')
        count[idx] += 1

count.sort()

one = 0
two = 0
if h%2 == 1 and w%2 == 1:
    one = 1
    two = (h-1+w-1) // 2
elif h%2 == 1 and w%2 == 0:
    two = w // 2
elif h%2 == 0 and w%2 == 1:
    two = h // 2

four = (h*w - one * 1 - two * 2) // 4
assert one + two*2 + four*4 == h*w

# 4つ組から順に考えれば良いのは、1,2,4が互いに倍数関係にあるから。
# 1人〜4人の組があって4人乗りのリフトに乗る問題があったな……あれは倍数関係に無いのでそれほど自明ではない……
# https://atcoder.jp/contests/dwacon2017-prelims/tasks/dwango2017qual_c

for i in range(26):
    temp = min(count[i]//4, four)
    count[i] -= temp * 4
    four -= temp
if four > 0:
    # 4つ組が取れないので不可
    print('No')
    exit()

for i in range(26):
    temp = min(count[i]//2, two)
    count[i] -= temp * 2
    two -= temp
if two > 0:
    # 2つ組が取れないので不可
    print('No')
    exit()

# 最後の1つは別に調べなくて良い
print('Yes')
