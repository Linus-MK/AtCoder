import copy
import sys

t, f = map(int, input().split())

letter_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, }
letter_set = "ABCDE"
lack_dict = {1: 23, 2: 5, 3: 1}

for _ in range(t):

	n = 0

	ans = []
	set_to_search = list(range(119))
	ans_string = ""

	for pos in range(1,4):
		count = [0] * 5
		set_list = [ [], [], [], [], [] ] 

		for sett in set_to_search:
			print(pos + 5 * sett)
			sys.stdout.flush()
			letter = input()
			n += 1 

			count[letter_dict[letter]] += 1
			set_list[letter_dict[letter]].append(sett)

		# countは24,24,23,24,24みたいになってる
		# countは6,6,0,5,6みたいになってる→minを探してはいけない

		index_lack = count.index(lack_dict[pos])

		set_to_search = copy.copy(set_list[index_lack])

		ans.append(index_lack)

		ans_string += letter_set[index_lack]

	print(4 + 5 * set_to_search[0])
	sys.stdout.flush()
	letter = input()

	for i in range(5):
		if (i not in ans) and (i != letter_dict[letter]):
			ans_string += letter_set[i]
			ans.append(i)

	for i in range(5):
		if (i not in ans):
			ans_string += letter_set[i]
			ans.append(i)

	# print(ans, file=sys.stderr)
	# print(n, file=sys.stderr)
	print(ans_string)
	sys.stdout.flush()
	result = input()
	if result != "Y":
		exit()

