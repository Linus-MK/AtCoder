n = int(input())
nums = list(map(int, input().split()))

print("YES" if len(set(nums)) == len(nums) else "NO")
