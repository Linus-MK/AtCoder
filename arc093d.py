"""
上半分を真っ黒、下半分を真っ白に塗る

その後、境界線に触れないように黒の内部に縦横1つおきに白マスを足していく。
同様に白の内部に黒マスを足していく。
100行10列でざっと50*100/(2*2) = 1250 個は置けるので、500個は構成できる！
→縦を50行にしました。それでも500個作れるので。
"""

white, black = list(map(int, input().split()))

print("50 100")

n_col = 100
for row_i in range(25):
	if row_i % 2 == 0:
		print("#" * n_col)
	else:
		if white > 1:
			white_in_row = min(49, white - 1) 
			print("#." * white_in_row + "#" * (n_col - 2 * white_in_row))
			white -= white_in_row
		else:
			print("#" * n_col)

for row_i in range(25):
	if row_i % 2 == 0:
		print("." * n_col)
	else:
		if black > 1:
			black_in_row = min(49, black - 1) 
			print(".#" * black_in_row + "." * (n_col - 2 * black_in_row))
			black -= black_in_row
		else:
			print("." * n_col)
