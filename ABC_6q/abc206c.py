n = int(input())
nums = list(map(int, input().split()))

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

ans = n * (n-1)//2
for k, v in freq.items():
    ans -= v * (v-1)//2
print(ans)
