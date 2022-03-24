# 先頭から見ていって、初めて減少する前の値
n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print('')
    exit()
for i in range(1, n):
    if nums[i-1] > nums[i]:
        del_value = nums[i-1]
        break
    if i == n-1:
        del_value = nums[n-1]
        break

new_nums = [str(i) for i in nums if i != del_value]
print(' '.join(new_nums))