n, x = list(map(int, input().split()))
nums = list(map(int, input().split()))

new_nums = [num for num in nums if num != x]
print(" ".join(map(str, new_nums)))