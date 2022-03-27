n = int(input())
nums = set(map(int, input().split()))

for i in range(2000+2):
    if i not in nums:
        print(i)
        exit()
