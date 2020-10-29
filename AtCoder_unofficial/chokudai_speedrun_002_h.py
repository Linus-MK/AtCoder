# 半信半疑で提出してしまったけど、正確な証明は以下の通り
# a == bのとき、余りは常に等しいので-1
# a > bとする。a < bも同様。
# a mod x = b mod x ⇔ (a-b) mod x = 0 より、題意を満たすこととxがa-bの約数であることは同値である。
# したがってxとして最大のものはa-bである。
import math
n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a == b:
        print(-1)
    else:
        print(abs(a-b))
