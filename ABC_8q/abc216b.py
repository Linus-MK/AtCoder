n = int(input())
nameset = set()
for i in range(n):
    te = input()
    nameset.add(te)

if len(nameset) < n:
    print("Yes")
else:
    print("No")
