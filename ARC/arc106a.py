n = int(input())

three = [3]
five = [5]

while True:
    t = three[-1] * 3
    if t > n:
        break
    three.append(t)

while True:
    f = five[-1] * 5
    if f > n:
        break
    five.append(f)

for t in range(len(three)):
    for f in range(len(five)):
        if three[t] + five[f] == n:
            print(f'{t+1} {f+1}')
            exit()

print(-1)
