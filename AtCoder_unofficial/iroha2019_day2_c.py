# 座標圧縮そのままの問題
# https://atcoder.jp/contests/abc036/tasks/abc036_c

zahyou = {}
arr = []
N = int(input())

for i in range(N):
	h = int(input())
	zahyou[h] = -1
	arr.append(h)

temp = sorted(zahyou)

sorted_zahyou = {}
for i in range(len(temp)): # 重複があると辞書が短くなるので、tange(N)では不可
	sorted_zahyou[temp[i]] = i+1 # 0始まり→1始まり

for i in range(N):
	print(sorted_zahyou[arr[i]])
