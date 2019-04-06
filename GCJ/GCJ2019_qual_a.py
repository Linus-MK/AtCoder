	# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

	N = int(input())
	for i in range(N):
		value = int(input())

		A = value
		B = 0
		strv = str(value)
		lenv = len(strv)
		for idx in range(lenv):
			if strv[idx] == "4":
				dif = 2 * (10 ** (lenv-idx -1) )
				A -= dif
				B += dif

		print("Case #{0}: {1} {2}".format(i+1, A, B) )
