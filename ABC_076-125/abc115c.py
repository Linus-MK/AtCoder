import numpy as np

n,k = map(int, input().split())

arr = []
for _ in range(n):
	arr.append(int(input()))

arr = np.sort(np.array(arr)) #昇順

print(
	(arr[(k-1):] - arr[:-(k-1)]).min() )

