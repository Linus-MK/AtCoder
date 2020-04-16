n = int(input())
nums = list(map(int, input().split()))

# これ直前に解いた Simplified mahjong とちょっと似てる?
# 重複している=取り除かなきゃいけない枚数の2の倍数切り上げ。

nums.sort()
sequential = 1
before = nums[0]
dup = 0
for i in nums[1:]:
    if i == before:
        sequential += 1
    else:
        dup += sequential - 1
        sequential = 1
    before = i

dup += sequential - 1

print(n - (dup + 1) // 2 * 2)
