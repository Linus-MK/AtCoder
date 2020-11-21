n = int(input())
s = input()

status = [-1]
n_del = 0
for char in s:
    if char == 'f':
        status.append(1)
    elif char == 'o':
        if status[-1] == 1:
            status[-1] = 2
        else:
            status = [-1]
    elif char == 'x':
        if status[-1] == 2:
            del status[-1]
            n_del += 1
        else:
            status = [-1]

    else:
        status = [-1]

print(n - n_del * 3)
