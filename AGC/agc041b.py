# うーん分からん
# ある特定の問題を入れたい人の気持ちになって考えた場合、トップにする必要はない
# 上位P問が使われるので、同率P位に滑り込めればOK

# 明らかに、ソートしても問題ない

# 投票して数字を増やすより減らしたほうが見通しが立てやすい気がするぞ
# （P問の値を1引き上げるのではなく、N-P問の値を1引き下げる、と考える。これでも同じ。）
# 降順にソートする。
# 「ある特定の問題」がk問目だとする。
# 上位（P-1）問は確定。P問目〜k-1問目をk問目と同じ数まで引き下げられたらOK。
# この引き下げが可能である条件は
# ・P問目の数 - k問目の数 <= 投票者の数M
# ・引き下げに必要な票数合計 <= 投票者の数M * 引き下げ票数(N-V)
# これが必要条件なのは分かるけど、十分性は……? この2つを満たせば必ず引き下げができるのか……?
# まぁ多分できそうな気がする

# 実際は毎回この判定をやると計算量が間に合わない
# 差分だけ調べて合計を更新する（累積和っぽい感じ）

n, m, v, p = list(map(int, input().split()))
vote = list(map(int, input().split()))
vote.sort(reverse=True)

target_score = vote[p-1]  # P問目

ans = p  # 最初p問は明らかに条件を満たす

vote_num_to_match = 0
# print(vote)
for i in range(p, n):

    vote_num_to_match += (vote[i-1] - vote[i]) * (i-(p-1))
    # print(vote_num_to_match)
    if target_score - vote[i] <= m and vote_num_to_match <= m * (n-v):
        ans += 1
    else:
        break

print(ans)
