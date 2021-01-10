# 疲れてどうこうを一切無視した場合
# まず初期状態で正解の荷物を持ってる人は考慮外でよい
# 各人が、「自分が持ってる荷物を本来持つべき人」を指差すと、有向の円環ができる。
# （逆に、「自分が本来持つべき荷物を持ってる人」から指差される）
# 指差している人と荷物を交換すると、指差している相手が正しい荷物を持って輪から抜ける、
# 基本的には正しい荷物をもつ人間は1人ずつ増えるが、最後の2人は一緒に解決するので
# 必要な交換回数は
# 輪それぞれについて「輪の人数 - 1」の合計
# あるいは初期状態で不正解の人の数 - 輪の数 と言い換えても良い

# で、疲れてどうこうする話。
# 初期状態で疲れているやつがいなければ実現可能である。
### (1) 輪の中で体重最小の人間に注目すると、この人が持っている荷物は全員が疲れずに持つことができる。
### したがって、この荷物を輪の全員に次々に1周回すように交換すれば、代位を満たす交換が実現できる。
### (2) もしくは、輪の中で体重最大の人間はすべての荷物を疲れずに持てるので、この人が全ての荷物を持つように交換しても良い。

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

