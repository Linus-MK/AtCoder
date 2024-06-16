# 2024/06/16
# お気持ち：
# 0以外が残った状態だとスコアが大幅悪化。→全部を0にして操作終了することがほぼ必須。
# 最後に左上に+1、右下に-1とかだと移動がキツい。→周りを優先的に埋めて終わらせていったほうがいい気がする。
# 盤面は20×20で固定→例えば4×4か5×5の小区画を考える。小区画AからCに80を移動する、とかは決め打ちしやすい。
# * 小区画どうしの移動量を決める
# * 小区画内部での移動量は勝手に決まるはず
# * ↑のもとで移動の具体的な様子を決める
# * 全体の順番を決める
# の3つを決めるとかね。

# んーこれ以上考えても動けないから、渦巻き状に外→内に回って、逆に回る決定論的なコードを書きまーす。

# seed 20
# 中央に行った時点で Cost = 183197 Diff = 540400 v = 804
# 最後で Cost = 257266 Diff = 0 v = 0
# 後半を蛇行型に変えて、Cost = 238502 Diff = 0 v = 0
# 積み荷が500に達したら中断して捨てに行くように変えて、Cost = 195614 Diff = 0 v = 0

import copy

n = int(input())
h = 20
w = 20
init_board = []
for i in range(h):
	temp = list(map(int, input().split()))
	init_board.append(temp)

board = copy.deepcopy(init_board)

move_length = [19]
for i in range(19, 0, -1):
	move_length.append(i)
	move_length.append(i)

direction = "RDLU" * 20
row_diff = {
	"R": 0,
	"D": 1,
	"L": 0,
	"U": -1
}
col_diff = {
	"R": 1,
	"D": 0,
	"L": -1,
	"U": 0
}

def move(r, c, r0, c0, ans_list):
	if r0 > r:
		x = ["D"] * abs(r0-r)
		ans_list.extend(x)
	if r0 < r:
		x = ["U"] * abs(r0-r)
		ans_list.extend(x)

	if c0 > c:
		x = ["R"] * abs(c0-c)
		ans_list.extend(x)
	if c0 < c:
		x = ["L"] * abs(c0-c)
		ans_list.extend(x)

	return ans_list

def load(amount, i, j, truck_dump, board, ans_list):
	truck_dump += amount
	board[i][j] -= amount
	ans_list.append("+" + str(amount))
	return truck_dump, board, ans_list

def unload(amount, i, j, truck_dump, board, ans_list):
	# amountは正の数
	# ここでは可能かどうか（積み荷が十分あるか）の判定をしていない
	truck_dump -= amount
	board[i][j] += amount
	ans_list.append("-" + str(amount))
	return truck_dump, board, ans_list

ans_list = []
truck_dump = 0
if board[0][0] > 0:
	z = board[0][0]
	truck_dump, board, ans_list = load(z, 0, 0, truck_dump, board, ans_list)
r = 0
c = 0
for peri_i in range(len(move_length)):
	for move_i in range(move_length[peri_i]):
		# 移動
		direction_char = direction[peri_i]
		ans_list.append(direction_char)
		r += row_diff[direction_char]
		c += col_diff[direction_char]
		# その高さが+ならばload、-ならば（可能な範囲で）unload
		if board[r][c] > 0:
			z = board[r][c]
			truck_dump, board, ans_list = load(z, r, c, truck_dump, board, ans_list)
		elif board[r][c] < 0:
			z = min(-board[r][c], truck_dump)
			if z == 0:
				continue
			truck_dump, board, ans_list = unload(z, r, c, truck_dump, board, ans_list)
	
	
	# ここで左上もしくは右上で、なおかつ積み荷がやたらと多い（※）場合は、現在位置よりも上方だけを対象に捨てに行く
	# ビジュアライザを見て決め打ちで500とする
	# 関数にしたいけどまぁ良いや
	too_much_dump = 500
	if (peri_i % 4 in [0, 3] and truck_dump >= too_much_dump):
		r_mem, c_mem = r, c
		for r0 in range(0, r):
			# 偶数列目は右から左に移動させる
			if r0 % 2 == 1:
				start, end, step = n-1, -1, -1
			else:
				start, end, step = 0, n, 1

			for c0 in range(start, end, step):

				if board[r0][c0] <0:
					ans_list = move(r, c, r0, c0, ans_list)
					r = r0
					c = c0
					z = min(-board[r][c], truck_dump)
					if z == 0:
						continue
					truck_dump, board, ans_list = unload(z, r, c, truck_dump, board, ans_list)
		
		# 元の位置に戻れ
		ans_list = move(r, c, r_mem, c_mem, ans_list)
		r, c = r_mem, c_mem

	# ここで左下もしくは右下で、なおかつ積み荷がやたらと多い（※）場合は、現在位置よりも下方だけを対象に捨てに行く
	# ビジュアライザを見て決め打ちで500とする
	# 関数にしたいけどまぁ良いや
	if (peri_i % 4 in [1, 2] and truck_dump >= too_much_dump):
		r_mem, c_mem = r, c
		for r0 in range(r+1, n):
			# 偶数列目は右から左に移動させる
			if r0 % 2 == 1:
				start, end, step = n-1, -1, -1
			else:
				start, end, step = 0, n, 1

			for c0 in range(start, end, step):

				if board[r0][c0] <0:
					ans_list = move(r, c, r0, c0, ans_list)
					r = r0
					c = c0
					z = min(-board[r][c], truck_dump)
					if z == 0:
						continue
					truck_dump, board, ans_list = unload(z, r, c, truck_dump, board, ans_list)
		
		# 元の位置に戻れ
		ans_list = move(r, c, r_mem, c_mem, ans_list)
		r, c = r_mem, c_mem

# 落としてなくてマイナスの値になっているところに、持ってる砂を落として、オール0にする
for r0 in range(n):
	# 偶数列目は右から左に移動させる
	if r0 % 2 == 1:
		start, end, step = n-1, -1, -1
	else:
		start, end, step = 0, n, 1

	for c0 in range(start, end, step):

		if board[r0][c0] <0:
			ans_list = move(r, c, r0, c0, ans_list)
			r = r0
			c = c0
			z = min(-board[r][c], truck_dump)
			if z == 0:
				continue
			truck_dump, board, ans_list = unload(z, r, c, truck_dump, board, ans_list)

for ans in ans_list:
	print(ans)