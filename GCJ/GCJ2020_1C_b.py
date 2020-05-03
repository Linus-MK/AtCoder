# 9, 10, 17
# 9, 19, 36点

# 10, 16, 16
# 10, 26, 42点

# すっげぇ虚仮威しにしか見えない問題だが……
# 最上位の桁が1が一番出現しやすくて、9が一番出現しにくい
# 0は最上位に唯一出現しない文字

N = int(input())
for ti in range(N):
    u = int(input())
    moji = [input().split() for i in range(10000)]

    kaisuu_dict = {}
    for i in range(10000):
        leftmost = moji[i][1][0]
        if leftmost in kaisuu_dict:
            kaisuu_dict[leftmost] = kaisuu_dict[leftmost] + 1
        else:
            kaisuu_dict[leftmost] = 1
        
    # 降順 多い方から少ない方に
    kaisuu_sorted = sorted(kaisuu_dict.items(), key=lambda x:x[1], reverse=True)

    # 0を探す
    for i in range(10000):
        rightmost = moji[i][1][-1]
        if rightmost not in kaisuu_dict:
            r = rightmost
            break

    ans = r
    for k in kaisuu_sorted:
        ans = ans + k[0]

    print("Case #{0}: {1}".format(ti+1, ans))