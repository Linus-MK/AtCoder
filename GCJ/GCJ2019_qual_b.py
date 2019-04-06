# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

N = int(input())
for i in range(N):
	size = int(input())
	route = input()
	ans = ""
	opponent_e = 0
	opponent_s = 0

	for idx in range(size - 1):

		if (opponent_e == idx and route[2*idx] == "E"):
			ans += "SE"
		elif (opponent_e + (1 if route[2*idx] == "E" else 0) == idx+1 and route[2*idx+1] == "S"):
			ans += "SE"
		else:
			ans += "ES"

		opponent_e += route[2*idx : 2*(idx+1) ].count("E")
		opponent_s += route[2*idx : 2*(idx+1) ].count("S")

	print("Case #{0}: {1}".format(i+1, ans) )
