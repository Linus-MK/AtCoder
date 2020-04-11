# URL
from statistics import mean

beams = [[0, -1], [0, 1], [1, 0], [-1, 0]]
N = int(input())
for ix in range(N):
    r, c = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(r)]

    ans = 0

    while True:
        # print(matrix)

        # そのラウンドのinterest levelを計算
        round_interest_level = 0
        for ri in range(r):
            round_interest_level += sum(matrix[ri])
        ans += round_interest_level
        # print(round_interest_level)

        # 各ダンサーについて、近傍ダンサーを計算、近傍ダンサーの平均を計算
        # 位置を示すタプルをキーとして、近傍ダンサーの得点をvalueにしよう
        di = {}
        for ri in range(r):
            for ci in range(c):
                if matrix[ri][ci] == 0:
                    continue
                # find 近傍ダンサー
                for beam in beams:
                    # 4方向に対して
                    r_pos = ri
                    c_pos = ci
                    while True:
                        r_pos += beam[0]
                        c_pos += beam[1]
                        if not (0 <= r_pos <= r-1 and 0 <= c_pos <= c-1):
                            # その方向にはいない
                            break
                        if matrix[r_pos][c_pos] > 0:
                            if (ri, ci) not in di:
                                di[(ri, ci)] = [matrix[r_pos][c_pos]]
                            else:
                                di.get((ri, ci), []).append(matrix[r_pos][c_pos])
                            break

        # elimination
        eliminated = False
        for key, values in di.items():
            ri = key[0]
            ci = key[1]
            my_score = matrix[ri][ci]
            neighbor_score = mean(values)  # ★
            if my_score < neighbor_score:
                # elimination
                matrix[ri][ci] = 0
                eliminated = True

        # eliminationする人がいないならbreak
        if not eliminated:
            break
        # break

    print("Case #{0}: {1}".format(ix+1, ans))
