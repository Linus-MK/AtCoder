n, m = list(map(int, input().split()))

wa_count = [0] * n
is_accepted = [False] * n
ans_ac = 0
ans_wa = 0

for i in range(m):
    p, s = input().split()
    p = int(p) - 1

    if s == 'AC':
        if not is_accepted[p]:
            is_accepted[p] = True
            ans_ac += 1
            ans_wa += wa_count[p]
    else:
        wa_count[p] += 1

print(ans_ac, ans_wa)
