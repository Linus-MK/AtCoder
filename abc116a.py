a,b,c = list(map(int, input().split()))

if a == max(a, b, c):
	print(b*c//2)
if b == max(a, b, c):
	print(c*a//2)
if c == max(a, b, c):
	print(a*b//2)
