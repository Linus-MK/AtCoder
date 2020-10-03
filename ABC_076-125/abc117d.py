# bitごとに独立に考えてよい。
# あるビットを反転するかどうか? = ある位に立っているビット数が全体の半数より多いか少ないか?
# K以下と言わず全体の最適なら各bitごとに考えて足しておしまい。
# しかしK以下に限定されている……

# 0以上K以下の整数Xを1個選ぶ
# ある位iのビットが0ならば、スコアに変化なし
# ある位iのビットが1ならば、スコア+=S_i ただしS_iは負の場合もある
# これを繰り返してXに対応するスコアを決める
# スコアの最大値は?
# K以下という成約がなければ、スコアが正のものだけ選べば終了。

# 0~1023のなかなら862 = '0b1101011110' が最高スコア
# だけど上限Kは852なので、10以上減らさねば
# -512, -256, -64, -16, -8-4, -8-2 のうちスコアが高いもの。


n, length = list(map(int, input().split()))
nums = list(map(int, input().split()))
