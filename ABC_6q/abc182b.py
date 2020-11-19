n = int(input())
nums = list(map(int, input().split()))

ans = 0
max_num_multiple = 0

for div in range(2, 1001):
    num_multiple = 0
    for num in nums:
        if num % div == 0:
            num_multiple += 1
    if num_multiple > max_num_multiple:
        max_num_multiple = num_multiple
        ans = div

print(ans)
