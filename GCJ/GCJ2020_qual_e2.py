# https://...

# N=6で試してみたら、22:49→23:09まで20分やっても答えが出なかったので諦めました。爆発的増加がヤバい。


from itertools import permutations

N = int(input())

# matrix = []
# perm_list = permutations(range(1, N+ 1)) 
# だとイテレータができるので、1回最後まで行くとそこで探索終了になる。リストにする必要あり。
perm_list = list(permutations(range(1, N+ 1)))
count = 0
trace_list = []

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
        trace = 0
        for ii in range(N):
            trace += matrix[ii][ii]
        if trace not in trace_list:
            trace_list.append(trace)
            print("trace: ", trace)
            print(matrix)

        count += 1


    else:
        for perm_new in perm_list:
            # print('appending...', n_row, list(perm_new) )
            check(matrix, n_row + 1, list(perm_new))


for perm in perm_list:
    check([], 0, list(perm))

print(count)
