n = int(input())

# n / y = a ... a
a = 1
ans = 0
while (a*a <= n):
	y = (n//a)-1
	if (n//a)*a == n and y>a:
		ans += y
	a+= 1

print(ans)
