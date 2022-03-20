_ = input()
s = input()
direction = 0
x = y = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for char in s:
    if char == 'S':
        x += dx[direction]
        y += dy[direction]
    else:
        direction += 1
        direction %= 4

print(f"{x} {y}")
