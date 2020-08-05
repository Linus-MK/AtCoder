x, n = list(map(int, input().split()))
nums = list(map(int, input().split()))

if x not in nums:
    print(x)
    exit()
for i in range(1, 200):
    if x-i not in nums:
        print(x-i)
        exit()
    if x+i not in nums:
        print(x+i)
        exit()
