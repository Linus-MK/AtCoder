# https://...


from itertools import permutations

N = int(input())

# matrix = []
perm_list = permutations(range(1, N+ 1))


def check(matrix, n_row, perm):
    # n_row は 0-index

    matrix.append(perm)
    print(n_row, matrix)

    # ラテン方陣として不適格か判定する
    for row in range(n_row):
        for col in range(N):
            if matrix[row][col] == matrix[n_row][col]:
                # 不適格
                return False

    if n_row == N-1:
        print('found a new laten matrix')
        print(matrix)
    else:
        for perm_new in perm_list:
            print('appending...', n_row, list(perm_new) )
            check(matrix, n_row + 1, list(perm_new))


for perm in perm_list:
    check([], 0, list(perm))
