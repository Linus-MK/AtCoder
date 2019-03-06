a = int(input())

for i in range(1,a+1):
	string = ''

	if i % 2 == 0:
		string += 'a'
	if i % 3 == 0:
		string += 'b'
	if i % 4 == 0:
		string += 'c'
	if i % 5 == 0:
		string += 'd'
	if i % 6 == 0:
		string += 'e'

	if string != '':
		print(string)
	else:
		print(i)
