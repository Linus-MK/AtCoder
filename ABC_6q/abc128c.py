n, m = list(map(int, input().split()))
switches = [list(map(int, input().split())) for i in range(m)]
ps = list(map(int, input().split()))

ans = 0
for idx in range(2**n):
    switch_on = [False] * n
    for s in range(n):
        if 2**s & idx > 0:
            switch_on[s] = True

    ok = True
    # ビット上位がN，下位が1
    for lamp in range(m):
        num_on_switch = 0
        for s in switches[lamp - 1][1:]:
            if switch_on[s-1] == True:
                num_on_switch += 1
        
        if num_on_switch % 2 != ps[lamp-1]:
            ok = False
        if not ok:
            break
    
    if ok:
        ans += 1

print(ans)
