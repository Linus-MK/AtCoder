# クエリが複数回与えられて、毎回のクエリに対する回答をする必要がある
# という時点で累積和を意識するべきだった……

# 競技中に一瞬思いついたが、10万の配列を作ったときにメモリが足りるかを懸念して避けてしまった
# 10万くらいなら余裕で足りるよ

# printしてみた配列の大きさ：
# 提出時の表示： 実行時間とメモリ 878 ms	6104 KB https://atcoder.jp/contests/abc122/submissions/4758777

N,Q =  map(int, input().split())
S = input()

cumsum = []
# cumsum[i] := (0-indexで)0文字目からi文字目までに含まれる部分列"AC"の個数
# (0-indexで)l文字目からr文字目までに含まれる部分列"AC"の個数は、cumsum[r] -cumsum[l]である
# l-1文字目とl文字目が"AC"になるケースも除外したいので、cumsum[l]を引くこと

cumsum.append(0)
summ = 0
for i in range(1,N):
	if S[i-1] == "A" and S[i] == "C":
		summ +=1
	cumsum.append(summ)

for _ in range(Q):
	left, right = map(int, input().split())
	left -= 1 # 1-indexから0-indexに変更する
	right -= 1
	print(cumsum[right] - cumsum[left])

