# 9, 10, 17
# 9, 19, 36点

# 10, 16, 16
# 10, 26, 42点

# 1まで正解、2つ目はアルゴリズム的にできてるけどTLEが取り除けず。

N = int(input())
for ti in range(N):
    n, d = list(map(int, input().split()))
    pieces = list(map(int, input().split()))

    if n >= 400:
        exit()

    pieces.sort()
    ans = d-1

    for denomi in range(1, d+1):
        for base in pieces:
            # 角度が base / denomi の場合
            num_cut = 0
            num_served = 0
            temp_q_list = [-999] * n
            is_just = [False] * n
            for i, now in enumerate(pieces):
                temp_q, temp_r = divmod(now * denomi, base)
                temp_q_list[i] = temp_q
                is_just[i] = (temp_r == 0)

            for temp_q, just in zip(temp_q_list, is_just):
                # ちょうど切れるやつだけ舐める
                if just:

                    if num_served + temp_q > d:
                        num_cut += (d - num_served)
                        num_served += (d - num_served)
                        break
                    else:
                        num_cut += temp_q - 1
                        num_served += temp_q
                        if num_served == d:
                            break
                
                # 枝刈り
                if num_cut >= ans:
                    break
            
            for temp_q, just in zip(temp_q_list, is_just):
                if not just:
                    ## ちょうどに切れないやつだけ舐める

                    if num_served + temp_q > d:
                        num_cut += (d - num_served)
                        num_served += (d - num_served)
                        break
                    else:
                        num_cut += temp_q
                        num_served += temp_q
                        if num_served == d:
                            break

                    # 枝刈り
                    if num_cut >= ans:
                        break

            # 全部切っても提供不能
            if num_served < d:
                continue
            else:
                ans = min(ans, num_cut)

    print("Case #{0}: {1}".format(ti+1, ans))

# 小さい方から（余りが出るものも出ないものも）順に取ると失敗する例
# 4 3
# 10 11 12 20
# 20を切って10-10とするのが正解(1回)だが、11と12を切ってしまい2回という出力になってしまう
