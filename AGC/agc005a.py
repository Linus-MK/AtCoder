# 前から順に見ていき、Tなら+1点、Sなら-1点とする。
# 最後まで見たときの途中の最高得点が、最後に残るTの個数。なので答えはその2倍。

# 理由：
# 最高得点a点とすると、その左側ではTがSよりもa個多いので、そのa個は消せない。右側にいくらSがあっても関係ない。
# その他が全部消える理由はイメージ的にはそんな気がするが、ちゃんとは分からない……

# 解説見たらスタックのpushとpopで説明してた。解説と違う解き方で解いてた。
s = input()
score = max_score = 0
for ch in s:
    if ch == "T":
        score += 1
        max_score = max(score, max_score)
    elif ch == "S":
        score -= 1
print(max_score * 2)
