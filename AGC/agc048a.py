# 難しかった……取っかかりが見えなかった……
# 「これ、大抵の場合は1文字目と2文字目をスワップすれば条件を満たすんじゃない? 2以上になるのってどんなとき?」というのが第一のポイント
# aじゃない文字のうち最初のものを1文字目に持ってくれば条件を満たす
# ここまでで提出してWA

# aaazは上記だとzaaaにして3となるが、正しくはazaaの2。
# tより後の文字のうち最初のものを2文字目に持ってくれば条件を満たす。小さい方を答えとすれば良い。これで正答。
# 質問：あれ、tを持ってきて条件を満たす場合もあるよね?
# →いいえ。ありません。3文字目以降のtを持ってくるということは最初2文字はaaなので、持ってきた後はata...となりatcoderより前です。

n = int(input())
for i in range(n):
    s = input()

    answer = 'atcoder'

    if s.count('a') == len(s):
        print(-1)
        continue
    
    if s > answer:
        print(0)
        continue

    ans = 10000
    for j in range(1, len(s)):
        if s[j] > 'a':
            ans = min(ans, j)
    for j in range(2, len(s)):
        if s[j] > 't':
            ans = min(ans, j-1)
    print(ans)
