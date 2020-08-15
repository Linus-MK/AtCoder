n, limit = list(map(int, input().split()))
permute = list(map(int, input().split()))
score = list(map(int, input().split()))

visited = [False] * n

ans = -10 ** 16

for i in range(n):
    if visited[i]:
        continue

    score_circle = []
    now = i
    while True:
        visited[now] = True
        score_circle.append(score[now])

        next_ = permute[now] - 1
        if visited[next_]:
            # 円環のできあがり
            break
        now = next_
    
    period = len(score_circle)

    score_circle *= 2
    # 累積和
    cumsum = [0] * (2 * period + 1)
    for j in range(1, 2*period+1):
        cumsum[j] = cumsum[j-1] + score_circle[j-1]
    
    p_sum_max = [-(10**15)] * (period + 1)
    for k in range(period):
        for ll in range(period):
            p_sum_max[ll] = max(p_sum_max[ll], cumsum[k+ll] - cumsum[k])
    
    ans = max([ans] + p_sum_max[1:min(period+1, limit+1)])

    q, resi = divmod(limit, period)

    if q >= 1:
        ans = max(ans, cumsum[period] * (q-1) + max(p_sum_max[1:]))
        ans = max(ans, cumsum[period] * (q) + max(p_sum_max[:resi + 1]))

        # print(p_sum_max[:resi + 1])

print(ans)
