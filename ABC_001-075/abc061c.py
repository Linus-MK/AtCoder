n, k = map(int, input().split())

array = []
for i in range(n):
    a, b = map(int, input().split())
    array.append([a, b])

array.sort(key=lambda x: x[0])
current_idx = 0
for integer, length in array:
    current_idx += length
    if current_idx >= k:
        print(integer)
        exit()
