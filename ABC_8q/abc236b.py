n = int(input())
nums = list(map(int, input().split()))
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

for i in range(1, n+1):
    if freq[i] == 3:
        print(i)
