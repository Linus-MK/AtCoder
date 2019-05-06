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
	r3 = ((ans56 - ( (r4<<14) + (r5<<11) + (r6<<9) ))>>18) & bit_mask #ビットシフトのほうが加算よりも優先度が低いのでカッコが必要
	
	print("{0} {1} {2} {3} {4} {5}".format(r1,r2,r3,r4,r5,r6) )

	result = int(input())
	if result != 1:
		exit()
