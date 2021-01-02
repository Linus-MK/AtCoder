a = int(input())

## (a-1) C 11を求める問題なので、二項係数ライブラリを使って良いのだが、
## 天邪鬼なのでこれだけなら普通に書いてもできるねということで、これでやってみた

ans = 1
for i in range(a-1, a-1-11, -1):
    ans *= i
for i in range(1, 1+11):
    ans //= i
print(ans)
