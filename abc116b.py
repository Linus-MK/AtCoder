n = int(input())

arr = [-1] * 1000000
arr[0] = n

for i in range(1, 1000000):
	arr[i] = arr[i-1] // 2 if arr[i-1] % 2 == 0 else arr[i-1] *3 + 1

	if i >= 3 and arr[i] == arr[i-3]:
		print(i + 1) #0->1 indexed
		break
