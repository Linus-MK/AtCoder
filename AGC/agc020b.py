# 典型的な「逆、最終状態から考える」問題。
# ある操作は他の操作の結果と独立に考えることができる。
# ありえる数はある区間になるので、区間の上限と下限を持っておいて、1つの操作について順次計算すれば良い。

n = int(input())
nums = list(map(int, input().split()))

ans = (2, 2)

for div in reversed(nums):
    lower = (ans[0] + div - 1) // div * div
    upper = ans[1] // div * div
    if not lower <= upper:
        print(-1)
        exit()
    
    ans = (lower, upper + div - 1)

print(f'{ans[0]} {ans[1]}')
