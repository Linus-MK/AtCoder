# https://...


from itertools import permutations

N = int(input())

# matrix = []
# perm_list = permutations(range(1, N+ 1)) 
# だとイテレータができるので、1回最後まで行くとそこで探索終了になる。リストにする必要あり。
perm_list = list(permutations(range(1, N+ 1)))
count = 0

def check(matrix_old, n_row, perm):
    # n_row は 0-index
    global perm_list
    global count

    matrix = matrix_old + [perm]
    # print(n_row, matrix)

    # ラテン方陣として不適格か判定する
    for row in range(n_row):
        for col in range(N):
            if matrix[row][col] == matrix[n_row][col]:
                # 不適格
                return False

    if n_row == N-1:
        # print('found a new laten matrix')
        # print(matrix)
        count += 1


    else:
        for perm_new in perm_list:
            # print('appending...', n_row, list(perm_new) )
            check(matrix, n_row + 1, list(perm_new))


for perm in perm_list:
    check([], 0, list(perm))

print(count)
