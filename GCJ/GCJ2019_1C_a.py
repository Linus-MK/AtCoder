N = int(input())
for i in range(N):
	a = int(input())

	opponents = [input() for _ in range(a)]
	relevant_ops_index = list(range(a))
	Decided = False
	answer = ""

	for turn in range(300):
		num_s = num_r = num_p = 0

		for index in relevant_ops_index:
			op = opponents[index]
			op_hand = op[(turn) % len(op)]

			if op_hand == "S":
				num_s += 1
			elif op_hand == "R":
				num_r += 1
			elif op_hand == "P":
				num_p += 1

		if num_p > 0 and num_r > 0 and num_s > 0:
			answer = "IMPOSSIBLE"
			Decided = True
			break
		elif num_p > 0 and num_r > 0 and num_s == 0:
			answer += "P"

			for j in range(len(relevant_ops_index)):
				index = relevant_ops_index[j]
				op = opponents[index]
				op_hand = op[(turn) % len(op)]

				if op_hand == "R":
					relevant_ops_index[j] = -1

			relevant_ops_index = [x for x in relevant_ops_index if x >= 0]

		elif num_p > 0 and num_r == 0 and num_s > 0:
			answer += "S"
			for j in range(len(relevant_ops_index)):
				index = relevant_ops_index[j]
				op = opponents[index]
				op_hand = op[(turn) % len(op)]

				if op_hand == "P":
					relevant_ops_index[j] = -1
			relevant_ops_index = [x for x in relevant_ops_index if x >= 0]

		elif num_p == 0 and num_r > 0 and num_s > 0:
			answer += "R"
			for j in range(len(relevant_ops_index)):
				index = relevant_ops_index[j]
				op = opponents[index]
				op_hand = op[(turn) % len(op)]

				if op_hand == "S":
					relevant_ops_index[j] = -1

			relevant_ops_index = [x for x in relevant_ops_index if x >= 0]

		elif num_p == 0 and num_r > 0 and num_s == 0:
			answer += "P"
			Decided = True
			break
		elif num_p > 0 and num_r == 0 and num_s == 0:
			answer += "S"
			Decided = True
			break
		elif num_p == 0 and num_r == 0 and num_s > 0:
			answer += "R"
			Decided = True
			break

	if not Decided:
		answer = "IMPOSSIBLE" # battle continues eternally 

	print("Case #{0}: {1}".format(i+1, answer) )

# ある時点で関係がある相手、ない相手をふるい分けたい
# 自分が勝つのが確定した相手はopponentsリストから削除? 
# 関係ある相手インデックスのリストを作る　range(a)から順次削除 ★採用

