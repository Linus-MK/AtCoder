n = int(input())
nums = list(map(int, input().split()))

print(' '.join(list(map(str, sorted(nums)))))
