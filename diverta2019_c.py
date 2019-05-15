n = int(input())
strings = [input() for _ in range(n)]

count_a_last = 0
count_b_first = 0
coincide = True
internal = 0
for s in strings:
	internal += s.count("AB")

	if s[0] == "B" and s[-1] == "A":
		count_a_last += 1
		count_b_first += 1
	elif s[0] == "B":
		count_b_first += 1
		coincide = False
	elif s[-1] == "A":
		count_a_last += 1
		coincide = False

concat = min(count_a_last, count_b_first)
if concat > 0 and coincide :
	concat -= 1
print(internal + concat)
