n = int(input())

cords = [list(map(int, input().split() )) for _ in range(n)]

cord_dif_dict = {}

for i in range(n):
	for j in range(n):
		if i == j:
			continue

		dif_tuple = (cords[i][0] - cords[j][0], cords[i][1] - cords[j][1])

		if dif_tuple in cord_dif_dict:
			cord_dif_dict[dif_tuple] += 1
		else:
			cord_dif_dict[dif_tuple] = 1

m = 0
for key in cord_dif_dict:
	if cord_dif_dict[key] > m:
		m = cord_dif_dict[key]

print(n - m)
# print(cord_dif_dict)