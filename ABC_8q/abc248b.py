a, b, k = list(map(int, input().split()))

count = 0
current = a

while True:
    if current >= b:
        print(count)
        exit()

    current *= k
    count += 1

