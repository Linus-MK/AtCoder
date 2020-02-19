n, k = list(map(int, input().split() ))

s = input()
s2 = s[:k-1] + s[k-1].lower() + s[k:]
print(s2)
