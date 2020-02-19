# L 以下の数のうち最大の2のべき数をtとする。t = 2 ** k とする。
# k は len(L)-1だね。

# a+bがt未満： 3 ** k 通り
# a+bがt以上L以下： いろいろ複雑！

L = input()
lenL = len(L) 
ans = 3 ** (lenL - 1)
mod = 10 ** 9 + 7

pow_2 = [1] * (lenL+1)
pow_3 = [1] * (lenL+1)

# 2の100000乗や3の100000乗を計算すると(10進数47700桁の計算をするので！)時間がかかる。
# なので、pow_3[n] = 3 ** n % mod となる表を作る

for i in range(1, lenL+1):
	pow_2[i] = pow_2[i-1] * 2 % mod
	pow_3[i] = pow_3[i-1] * 3 % mod

num_one_leftside = 1
for i in range(1, lenL):
	if L[i] == '1':
		ans += pow_2[num_one_leftside] * pow_3[lenL - i - 1]
		ans %= mod

#		print (num_one_leftside ,  (lenL - i - 1))
		num_one_leftside += 1

ans += pow_2[num_one_leftside]
ans %= mod

print(ans)