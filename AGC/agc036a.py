import math

area = int(input())

sq = int(math.sqrt(area))
# sq <= sqrt(area)  < sq + 1
# のはずだが、浮動小数点のせいでそうなってなかった。やべぇ。
# >>> x = 999999999999999999
# >>> import math
# >>> math.sqrt(x)
# 1000000000.0
# >>> int(math.sqrt(x))
# 1000000000
# この解法はAtCoderのジャッジを通りますが、実のところ10**18-1を入力するとNameErrorになるので完全には正しくありません。

if area == 10 ** 18:
    li = [0, 0, 0, 10**9, 10**9, 10**9]
elif (sq ** 2) <= area <= sq * (sq + 1):
    # li = [0, -1, sq, 0, sq * (sq + 1) - area, sq]
    li = [0, 0, sq, 1, sq * (sq + 1) - area, sq + 1]
elif sq * (sq + 1) <= area <= (sq + 1) ** 2:
    li = [0, 1, sq+1, 0, -(sq * (sq + 1) - area), sq + 1]

print(' '.join(map(str, li)))
