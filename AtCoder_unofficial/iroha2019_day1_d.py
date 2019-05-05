n, x, y = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(n):
	if i%2 == 0:
		x+= arr[i]
	else:
		y+= arr[i]

if x>y:
	print("Takahashi")
elif x<y:
	print("Aoki")
else:
	print("Draw")
