import string

nums = list(map(int, input().split()))
ans_str = [string.ascii_lowercase[i-1] for i in nums]
print("".join(ans_str))

