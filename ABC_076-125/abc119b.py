N = int(input())
amount = 0
for i in range(N):
	x,u = input().split()
	x = float(x)
	# https://docs.python.org/ja/3/library/stdtypes.html#typesnumeric
	# double(x) は存在しない

	if u == "JPY":
		amount += x
	else:
		amount += x * 380000.0

print(amount)
