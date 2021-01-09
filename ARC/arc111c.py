# 疲れてどうこうを一切無視した場合
# まず初期状態で正解の荷物を持ってる人は考慮外でよい
# 各人が、「自分が持ってる荷物を本来持つべき人」を指差すと、有向の円環ができる。
# （逆に、「自分が本来持つべき荷物を持ってる人」から指差される）
# 指差している人と交換すると、指差している相手が輪から抜ける、最後の2人は一緒に解決するので
# 必要な交換回数は
# 輪それぞれについて「輪の人数 - 1」の合計
# あるいは初期状態で不正解の人の数 - 輪の数 といっても良い

# で、疲れてどうこうする話。
# 初期状態で疲れているやつがいなければ実現可能。
# 輪の中で体重最小のやつが持っている荷物をぐるっと回すように交換すればよい


n = int(input())
body_weight = list(map(int, input().split()))
baggage_weight = list(map(int, input().split()))
permute = list(map(int, input().split()))
permute = [p-1 for p in permute] # 1→0-index

visited = [False] * n
ans_num = 0
ans_oper = []
valid = True

for i in range(n):
    if permute[i] == i:
        # 初期状態で正解の荷物を持ってる
        visited[i] = True
        continue
    else:
        if not visited[i]:
            visited[i] = True
            circle = []
            circle.append(i)
            me = i
            while True:
                next_ = permute[me]
                visited[next_] = True
                if next_ == i:
                    break
                circle.append(next_)
                me = next_

            # circle1周する、
            minimum_body_weight = 10**9 + 10
            minimum_body_weight_idx = -1
            for idx, person in enumerate(circle):
                if body_weight[person] <= baggage_weight[permute[person]]:
                    # もう疲れてる
                    valid = False
                if body_weight[person] < minimum_body_weight:
                    minimum_body_weight = body_weight[person]
                    minimum_body_weight_idx = idx
            
            for j in range(len(circle) - 1):
                ans_oper.append([circle[minimum_body_weight_idx-j], circle[minimum_body_weight_idx-j-1] ])

            ans_num += len(circle) - 1

if valid:
    print(ans_num)

    for oper in ans_oper:
        print(f'{oper[0]+1} {oper[1]+1}')

else:
    print(-1)

