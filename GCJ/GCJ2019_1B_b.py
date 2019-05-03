# visible

t, w = map(int, input().split())
if w != 6:
	exit()

for _ in range(t):
	print(1)
	ans1 = int(input())
	print(2)
	ans2 = int(input())
	print(3)
	ans3 = int(input())
	print(4)
	ans4 = int(input())
	print(5)
	ans5 = int(input())
	print(6)
	ans6 = int(input())

	p = ans2 - ans1 # 2*r1 + r2
	q = ans6 - 2 * ans3 # 48*r1 + 4*r2

	r1 = int((q-p*4)/40)
	r2 = int(p - r1*2)
	r3 = int(ans3-ans2 - 4*r1)
	r4 = int((2*ans4-ans6 + 32*r1)/2)
	r5 = int((2*ans5-ans6) /2-r4)
	r6 = int(ans1 - (2*r1+r2+r3+r4+r5))

	print("{0} {1} {2} {3} {4} {5}".format(r1,r2,r3,r4,r5,r6) )

	result = int(input())
	if result != 1:
		exit()
