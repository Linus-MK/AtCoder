from operator import itemgetter
n, m = list(map(int, input().split() ))
values = list(map(int, input().split() ))
values.sort()

card_change = [list(map(int, input().split() )) for _ in range(m)]
card_change.sort(key = itemgetter(1))
# 変更後の数をkeyとしてソート

# X枚書き換えるとして、Xを全探索する方針で書いてみる
now = sum(values)
ans = sum(values)
idx = m - 1
for x in range(n):
	now -= values[x]

	card_change[idx][0] -= 1 # 変更可能枚数
	now += card_change[idx][1] # 変更後の値

	if now > ans:
		ans = now

	if card_change[idx][0] == 0:
		idx -= 1
		if idx < 0:
			break

print(ans)
