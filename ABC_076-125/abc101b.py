str_n = input()
n = int(str_n)

digit_sum = 0
for i in range(len(str_n)):
	digit_sum += int(str_n[i])
print("Yes" if n % digit_sum == 0 else "No")
