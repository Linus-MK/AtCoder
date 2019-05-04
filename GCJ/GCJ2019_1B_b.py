# visible+hidden
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122837#
t, w = map(int, input().split())

bit_mask = 0b1111111 #127, binary
import sys

for _ in range(t):
	print(210)
	ans210 = int(input())
	print(56)
	ans56 = int(input())

	r4 = ans210 >> 52
	r5 = (ans210 >> 42) & bit_mask
	r6 = (ans210 >> 35) & bit_mask

	r1 = ans56 >> 56
	r2 = (ans56 >> 28) & bit_mask
	r3 = ((ans56 - (r4<<14 + r5<<11 + r6<<9))>>18) & bit_mask
	r3 = ((ans56 - (r4*(2**14) + r5*(2**11) + r6*(2**9)))>>18) & bit_mask
	r3_2 = ((ans56 )>>18) & bit_mask
# 引いた効果が出ていない（=直上の2行が同じことをしている）ように見える。なんでや……
	
	if r3 != r3_2:
		print("{0} {1}".format(r3,r3_2), file=sys.stderr)
	print("{:b}".format(ans56), file=sys.stderr)

	print("{0} {1} {2} {3} {4} {5}".format(r1,r2,r3,r4,r5,r6) )

	result = int(input())
	if result != 1:
		exit()


'''
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
'''