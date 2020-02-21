h, w = list(map(int, input().split()))

temp = 0
for i in range(h):
    temp += input().count('#')
print("Possible" if temp == h+w-1else "Impossible")

'''
解説にもある通り、「問題文およびaで与えられる情報と整合するような駒の動き方が存在する。」　がポイント。もしこれがなかったら、
4 5
##...
#.#..
#..#.
...##
のような入力もありえることになる。
その時は「現在のマスの右または下の一方だけが#か? → Yesならそこに移動」を繰り返し、右下のマスに行ければPossible、かな。
'''
