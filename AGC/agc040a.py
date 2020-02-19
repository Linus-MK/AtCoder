# 最大で50万×2 = 100万なので間に合うかと思ったが、実行時間347 msと余裕だった。

arr = input()
l = len(arr)

ans_arr = [0] * (l+1)
for i in range(l):
    if arr[i] == '<':
        ans_arr[i+1] = ans_arr[i] + 1

for i in range(l-1, -1, -1):
    if arr[i] == '>':
        ans_arr[i] = max(ans_arr[i], ans_arr[i+1] + 1)

# print(ans_arr)
print(sum(ans_arr))
