s = input()

a = int(s[0:2])
b = int(s[2:4])

if 1 <= a <= 12 and  1 <= b <= 12:
	print("AMBIGUOUS")
elif 1 <= a <= 12 and  not (1 <= b <= 12):
	print("MMYY")
elif not(1 <= a <= 12) and  1 <= b <= 12:
	print("YYMM")
else:
	print("NA")

