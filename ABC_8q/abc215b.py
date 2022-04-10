n = int(input())

for i in range(0, 100):
    if 2**i > n:
        print(i-1)
        exit()