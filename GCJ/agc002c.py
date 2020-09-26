
n, length = list(map(int, input().split()))
nums = list(map(int, input().split()))

idx = -1
for i in range(n-1):
    if nums[i] + nums[i+1] >= length:
        idx = i
        break
if idx < 0:
    print('Impossible')
    exit()

print('Possible')
for i in range(idx):
    print(i+1)
for i in reversed(range(idx, n-1)):
    print(i+1)

