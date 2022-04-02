n = int(input())
nums = list(map(int, input().split()))

cut_pos = [0]
current_angle = 0
for num in nums:
    current_angle += num
    current_angle %= 360
    cut_pos.append(current_angle)


cut_pos.sort()
cut_pos.append(360)

max_ = 0
for i in range(n+1):
    size = cut_pos[i+1] - cut_pos[i]
    max_ = max(max_, size)
print(max_)
