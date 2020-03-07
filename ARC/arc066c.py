n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

valid = True
t = n-1
for i in range(n):
	if arr[i] != t :
		valid = False
	if i % 2 == 1 :
		t -= 2 

if not valid:
	print(0)
else:
	print(2 ** (n//2) % (10 ** 9 + 7))
