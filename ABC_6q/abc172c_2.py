# 二通りのやり方で解いてみよう。
# Aそれぞれに対してBを二分探索→M(累積和構成) + NlogM
# Aを昇順、Bを降順に動かす→O(N+M) このコードはこっち★ 240ms

n, m, k = list(map(int, input().split()))
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

time_sum = sum(bb)

a_idx = 0
b_idx = m-1
ans = 0

# 最初はA無し、B全部からスタート
book_num = m
while True:
    if time_sum > k:

        if b_idx < 0:
            break
        time_sum -= bb[b_idx]
        b_idx -= 1
        book_num -= 1
    else:
        # 実行可能な読み方
        ans = max(ans, book_num)
        
        if a_idx > n-1:
            break
        time_sum += aa[a_idx]
        a_idx += 1
        book_num += 1

print(ans)
