# https://img.atcoder.jp/abc138/editorial.pdf
# https://www.youtube.com/watch?v=lWETOlGiuaI
# このコードは公式解説動画をまんまpythonにしたものです。

# 解説動画
# s = abacaababc (10文字)の場合は
# a: [0, 2, 4, 5, 7, 10, 12, 14, 15, 17]
# b: [1, 6, 8, 11, 16, 18]
# c: [3, 9, 13, 19]
# という二重配列をまず作る。

# 例えばt = 'bbcca'だと
# 現在位置0、bを探す→1
# 現在位置1、bを探す→6
# 現在位置6、cを探す→9
# 現在位置9、cを探す→13(3に戻す)
# 現在位置3、aを探す→4
# で答えは14。
# C++のlower_boundは、「指定された要素『以上』の値が現れる最初の位置」なので、

# 解説pdf曰く：
# next(ch, i):=「s'のi文字目以降で文字種chが最初に現れる位置」を
# をO(文字種数×|S|)かけて事前に全て求める

# 文字の先頭に戻る可能性があるので、2回連結しておくと処理が楽になる

from bisect import bisect_left

s = input()
t = input()
n = len(s)
m = len(t)

index_list = [[] for _ in range(26)]

for i in range(n):
    index_list[ord(s[i]) - ord('a')].append(i)
for i in range(n):
    index_list[ord(s[i]) - ord('a')].append(i+n)

p = 0  # p以降
ans = 0
for j in range(m):
    ch = ord(t[j]) - ord('a')
    if len(index_list[ch]) == 0:
        # t内に出現する文字が、sに全く登場しないので、不可
        print(-1)
        exit()
    next_pos = bisect_left(index_list[ch], p)
    p = index_list[ch][next_pos] + 1
    # TODO: テーブルの正確な意味、二分探索の正確な意味、+1の意義あたり、ちゃんとわかってない。
    if p >= n:
        p -= n
        ans += n
    # print(p)

ans += p
print(ans)

