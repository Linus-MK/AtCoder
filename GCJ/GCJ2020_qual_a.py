# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9?show=progress

N = int(input())
for ix in range(N):
    size = int(input())
    matrix = [list(map(int, input().split())) for j in range(size)]

    trace = 0
    for i in range(size):
        trace += matrix[i][i]

    row_duplicate = 0
    for i in range(size):
        row_duplicate += len(set(matrix[i])) < size
    
    col_duplicate = 0
    for i in range(size):
        nums = []
        for row in range(size):
            nums.append(matrix[row][i])
        col_duplicate += len(set(nums)) < size

    print("Case #{0}: {1} {2} {3}".format(ix+1, trace, row_duplicate, col_duplicate))
