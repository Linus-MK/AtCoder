# PDFで解法が4つも書いてある。これはその最初の解法

x,y,z,k =  list(map(int, input().split() ))

aa = list(map(int, input().split() ))
bb = list(map(int, input().split() ))
cc = list(map(int, input().split() ))

aa.sort(reverse = True)
bb.sort(reverse = True)
cc.sort(reverse = True)
# 降順＝大きい方から順

ab = [i + j for i in aa for j in bb]
# appendを使うと遅いので、二重の内包記法を使う 
# 外側でaaの要素、内側でbbの要素が動いていく。今回はどっちでも良いけど。
ab.sort(reverse = True)

max_len = min(k, len(ab))
abc = [i + j for i in ab[:max_len] for j in cc]
abc.sort(reverse = True)

for i in range(k):
	print(abc[i])
