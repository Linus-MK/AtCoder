N = int(input())
arr = []

for _ in range(N):
	arr.append(int(input()) )

print (sum(arr) - int(max(arr)/2) )