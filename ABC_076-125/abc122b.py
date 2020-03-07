string = input()


ans = 0
section = 0
for i in range(len(string)):
	if string[i] in 'ATGC':
		section += 1
	else:
		if ans < section:
			ans = section
		section = 0

if ans < section:
	ans = section

print(ans)