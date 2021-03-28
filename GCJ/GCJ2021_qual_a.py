# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c

# 言われたことをそのまま再現すればよい。

N = int(input())
for i_test in range(N):

    length = int(input())
    array = list(map(int, input().split()))

    cost = 0
    for i in range(length-1):
        for j in range(i, length):
            if array[j] == i+1:
                cost += (j-i+1)
                array = array[0:i] + list(reversed(array[i:j+1])) + array[j+1:]

    print("Case #{0}: {1}".format(i_test+1, cost))
