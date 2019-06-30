s = input()

if s[0] == s[1] != s[2] == s[3] :
	print("Yes")
elif s[0] == s[2] != s[1] == s[3]:
	print("Yes")
elif s[0] == s[3] != s[2] == s[1]:
	print("Yes")
else:
	print("No")	