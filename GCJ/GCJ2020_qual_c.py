# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

N = int(input())
for i in range(N):
    in_str = input()
    depth_prev = 0
    ans_str = ''

    for j in in_str:
        d = int(j)
        if depth_prev < d:
            ans_str += '(' * (d - depth_prev)
        elif depth_prev > d:
            ans_str += ')' * (depth_prev - d)

        ans_str += j
        depth_prev = d

    ans_str += ')' * d

    print("Case #{0}: {1}".format(i+1, ans_str))
