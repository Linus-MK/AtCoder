import string
# bit全探索
n, k = list(map(int, input().split()))
strs = []
for i in range(n):
    strs.append(input())

ans = 0
for idx_bit in range(2**n):
    selected = []
    for idx_s in range(n):
        if idx_bit  & (2**idx_s):
            selected.append(strs[idx_s])
    
    num_of_ch = 0
    for ch in string.ascii_lowercase:
        count = 0
        for s in selected:
            if ch in s:
                count += 1
        if count == k:
            num_of_ch += 1
    ans = max(ans, num_of_ch)

print(ans)
