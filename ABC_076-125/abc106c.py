s = input()
k = int(input())
l = len(s)

first = ''
pos = l # 入力が1だけで構成されている場合に備えて必要
for i in range(l):
	if s[i] != '1':
		first = s[i]
		pos = i
		break

print('1' if k <= pos else first)
