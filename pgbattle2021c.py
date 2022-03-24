n = int(input())
ranks = list(map(int, input().split()))

dic = dict()

for idx, rank in enumerate(ranks):
    if dic.get(rank):
        dic[rank].append(idx+1)
    else:
        dic[rank] = [idx+1]

ok = True
for k, v in dic.items():
    if k == 1:
        if len(v) != 1:
            ok = False
    else:
        if len(v) != k//2:
            ok = False
if not ok:
    print(-1)
    exit()

ans = dic[1]

# ベストRを入れて長さを2倍にする
for k in range(1, n+1):
    best = 2**k
    ans_next = [-1] * best
    added = dic[best]

    for i in range(best//2):
        ans_next[i*2] = ans[i]
        ans_next[i*2+1] = added[i]
    
    ans = ans_next.copy()

str_ans = map(str, ans)
print(' '.join(str_ans))
