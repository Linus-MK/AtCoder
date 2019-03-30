# クエリが複数回与えられて、毎回のクエリに対する回答をする必要がある
# という時点で累積和を意識するべきだった……

# 競技中に一瞬思いついたが、10万の配列を作ったときにメモリが足りるかを懸念して避けてしまった
# 10万くらいなら余裕で足りるよ

# printしてみた配列の大きさ：約800000バイト
# 提出時の表示： 実行時間とメモリ 853 ms	6084 KB https://atcoder.jp/contests/abc122/submissions/4758805

N,Q =  map(int, input().split())
S = input()

cumsum = [0] * N
# cumsum[i] := (0-indexで)0文字目からi文字目までに含まれる部分列"AC"の個数
# (0-indexで)l文字目からr文字目までに含まれる部分列"AC"の個数は、cumsum[r] -cumsum[l]である
# l-1文字目とl文字目が"AC"になるケースも除外したいので、cumsum[l]を引くこと

summ = 0
for i in range(1,N):
	if S[i-1] == "A" and S[i] == "C":
		summ +=1
	cumsum[i] = summ

for _ in range(Q):
	left, right = map(int, input().split())
	left -= 1 # 1-indexから0-indexに変更する
	right -= 1
	print(cumsum[right] - cumsum[left])

# import sys
# print(sys.getsizeof(cumsum))
# 10000文字を入力した場合の表示結果が80064。 (8×要素数+64)バイトであろう。
# 制約上限の100000文字で800000バイトなので、10^9バイトの制限には余裕で収まる。
