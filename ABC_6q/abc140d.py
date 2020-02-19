n, k = list(map(int, input().split() ))
string = input()

n_katamari = 1

for i in range(n-1):
	if string[i] != string[i+1]:
		n_katamari += 1

n_katamari -= 2 * k
if n_katamari < 1:
	n_katamari = 1 

print(n - n_katamari)
