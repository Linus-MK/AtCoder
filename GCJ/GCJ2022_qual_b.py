# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
# You were given three printers and will use each one to print one of the D's.
# なので、3台のプリンターを1回ずつ使わなければいけない。1台のプリンターから2回は不可。

N = int(input())
for i_test in range(N):

    ink_amount = []
    for i in range(3):
        temp = list(map(int, input().split()))
        ink_amount.append(temp)

    # ink_min = [min(temp) for temp in ]
    ink_min = []
    for i in range(4):
        temp = [printer[i] for printer in ink_amount]
        ink_min.append(min(temp))

    if sum(ink_min) >= 10**6:
        if sum(ink_min[:3]) <= 10**6:
            ink_min[3] = 10**6 - sum(ink_min[:3])
        else:
            ink_min[3] = 0
            if sum(ink_min[:2]) <= 10**6:
                ink_min[2] = 10**6 - sum(ink_min[:2])
            else:
                ink_min[2] = 0
                ink_min[1] = 10**6 - ink_min[0]

        ink_min_str = list(map(str, ink_min))
        ans_str = " ".join(ink_min_str)
        print("Case #{0}: {1}".format(i_test+1, ans_str))
    else:
        print("Case #{0}: IMPOSSIBLE".format(i_test+1))
