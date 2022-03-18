h, w = list(map(int, input().split()))
mat = []
for i in range(h):
    temp = list(map(int, input().split()))
    mat.append(temp)
for i in range(w):
    temp = [row[i] for row in mat]
    temp_str = list(map(str, temp))
    print(' '.join(temp_str))
