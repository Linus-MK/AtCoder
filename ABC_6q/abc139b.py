a, b = map(int, input().split())

# 1 + (a-1) * i >= b
for i in range(30):
    if 1 + (a-1) * i >= b:
        print(i)
        exit()
