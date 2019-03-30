import bisect

N,Q =  map(int, input().split())
S = input()

start = []
end = []

for i in range(N-1):
	if S[i] == "A" and S[i+1] == "C":
		start.append(i)
		end.append(i+1)

length = len(start)
for _ in range(Q):
	left, right = map(int, input().split())
	left -= 1 # 1-indexから0-indexに変更する
	right -= 1

	if length == 0:
		print(0)
	else:
		# startの中で、left以上であるものの最小インデックス

		l1 = bisect.bisect_left(start, left)
		r1 = bisect.bisect_right(end, right) - 1

		print (r1-l1+1)

'''

	r = length
	l = 0
	c = int((r+l)//2)
	while(l<r):

		if start[c] >= left:
			r = c
			c = int((r+l)//2)
		else:
			l = c
			c = int((r+l)//2)

	X1 = c

	# endの中で、right以下であるものの最大インデックス
	r = length
	l = 0
	c = int((r+l)//2)
	while(l<r):

		if end[c] > right:
			r = c
			c = int((r+l)//2)
		else:
			l = c
			c = int((r+l)//2)

	X2 = c

	print(X2-X1+1)
'''