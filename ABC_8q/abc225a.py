n = list(input())
size = len(set(n))
if size == 1:
    print(1)
elif size == 2:
    print(3)
else:
    print(6)
