# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155

# 適当に（Googleの!）スプレッドシート使って、状況を再現した。ただし100人10000問を30人100問と小規模にした。
# めんどいから一様分布の代わりに等差数列にしたけど。

# チートの人は、普通に解いたときの正解確率をpをすると、チートを使ったときの正解率は(1+p)/2になる。
# 合計正解数が最も多い人か? → これはチーターのスキルが低いと、スキルの高い人間にスコアで負ける。
# 試しにこれでやってみるか。部分点解法がこれな気がする。→正解。部分点をこれで取れた。
# スキル3の人は100問中88.7問解ける。一方、チーターのスキルが2だと89.3問とこれより多く解ける。
# チーターのスキルも一様乱数に従うので、1/6の確率でスキル2以上であり、全体の中で正解数トップになる。これは正解条件である10%より高い。

N = int(input())
P = int(input())
for i_test in range(N):

    high_score = 0
    high_score_player = -1

    for i in range(100):
        s = input()
        correct_count = s.count('1')

        if correct_count > high_score:
            high_score = correct_count
            high_score_player = i
    

    print("Case #{0}: {1}".format(i_test+1, high_score_player + 1))
