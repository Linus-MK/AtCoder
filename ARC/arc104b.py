n, s  = input().split()
n = int(n)

cumsum_at = [0] * (n+1)
cumsum_cg = [0] * (n+1)

# cumsum[-1]は0なのでOK
for idx, char in enumerate(s, start=1):
    if char == 'A':
        cumsum_at[idx] = cumsum_at[idx-1] + 1
        cumsum_cg[idx] = cumsum_cg[idx-1]
    elif char == 'T':
        cumsum_at[idx] = cumsum_at[idx-1] - 1
        cumsum_cg[idx] = cumsum_cg[idx-1]
    elif char == 'C':
        cumsum_cg[idx] = cumsum_cg[idx-1] + 1
        cumsum_at[idx] = cumsum_at[idx-1]
    elif char == 'G':
        cumsum_cg[idx] = cumsum_cg[idx-1] - 1
        cumsum_at[idx] = cumsum_at[idx-1]

ans = 0
for i in range(n+1):
    for j in range(i+1, n+1):
        if cumsum_at[i] == cumsum_at[j] and cumsum_cg[i] == cumsum_cg[j]:
            ans += 1
print(ans)

