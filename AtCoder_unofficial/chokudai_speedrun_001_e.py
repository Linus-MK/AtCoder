n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    if nums[i] == 1:
        print(i+1)
