# aが1〜Nの整数、bがN〜1の整数だったら、和は全て同じ。
# そこから、例えば5番目だけ大きくしたいなら、a5〜aNとb1〜b5までにtを足せば良い。a5+b5は2t増えて、他はt増える。
# 最大にしたいところにN足して、次に大きくしたいところにN-1足して、以下同様。
# この「ある区間に一定要素を足す」は……imosすればよい。最初と最後だけメモっておいて最後に累積和。

n = int(input())
indices = list(map(int, input().split()))

a_diff = [1] * n # 1〜Nの差分をここに書いちゃう
b_diff = [-1] * n

for plus, idx in enumerate(indices):
    idx -= 1
    a_diff[idx] += plus
    # a_diff[最終要素の次] -= plus は不要。

    b_diff[0] += plus
    if idx +1 < n:
        b_diff[idx+1] -= plus

a = []
now = 1
for i in range(n):
    now += a_diff[i]
    a.append(now)

b = []
now = n+1
for i in range(n):
    now += b_diff[i]
    b.append(now)

print(' '.join(map(str, a)))
print(' '.join(map(str, b)))
