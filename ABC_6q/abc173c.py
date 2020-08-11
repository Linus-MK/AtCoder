h, w, k = list(map(int, input().split()))

masu = [input() for _ in range(h)]

ans = 0
for idx_h in range(2 ** h):
    for idx_w in range(2 ** w):
        m = masu.copy()
        for i_row, row in enumerate(m):
            for j_col, col in enumerate(row):
                if idx_h & (2 ** i_row) > 0 or idx_w & (2 ** j_col) > 0:
                    # m[i_row][j_col] = 'r'
                    m[i_row] = m[i_row][:j_col] + 'r' + m[i_row][j_col+1:]
        
        count_black = sum(map(lambda x: x.count('#'), m))
        if count_black == k:
            ans += 1

print(ans)
