# N個を選んだ和が合成数になるようにしたい
# →N個の和がNの倍数にすればよい
# →N個がすべて、Nで割った余りが等しいものにすればよい

# 5で割って1余る素数（1の位が1の素数）を挙げれば良い
def is_primary(n):
    k = 2
    while k*k <= n:
        if n % k == 0:
            return False
        k += 1
    return True

n = int(input())

count = 0
ans = []
for i in range(11, 5001, 10):
    if is_primary(i):
        ans.append(i)
        count += 1
        if count == n:
            break

print(" ".join(map(str, ans)))
