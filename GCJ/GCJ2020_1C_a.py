N = int(input())
for ti in range(N):
    temp = input().split()
    x = int(temp[0])
    y = int(temp[1])
    move = temp[2]

    ans = 'IMPOSSIBLE'
    for i in range(len(move)):
        if move[i] == 'N':
            y += 1
        elif move[i] == 'S':
            y -= 1
        elif move[i] == 'E':
            x += 1
        elif move[i] == 'W':
            x -= 1
        
        if abs(x) + abs(y) <= i+1:
            ans = i+1
            break

    print("Case #{0}: {1}".format(ti+1, ans))

