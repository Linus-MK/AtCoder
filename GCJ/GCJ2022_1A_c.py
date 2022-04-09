# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa9280
# 愚直に全探索
# 組み合わせが爆発しそうで困る

import itertools

def suitable(stack, weights, n_wei):
    ans = True
    for w in range(n_wei):
        if stack_dict[w] > weights[w]:
            ans = False
    return ans

def dfs(idx_ex, order, stack, stack_dict, n_ope):

    # 乗せる
    for w in (order):
        stack.append(w)
        stack_dict[w] = stack_dict[w] + 1
        n_ope += 1

    # ここでトレーニング！
    # 最後の場合はここでreturn
    if idx_ex == n_ex-1:
        return n_ope + len(stack)
    else:
        idx_ex += 1

    ans = 99999
    weights = weights_require[idx_ex]
    # weights = list(map(int, input().split()))

    # 余分なものがなくなるまで、上から取り除く
    while True:
        if suitable(stack, weights, n_wei):
            break
        stack_dict[stack[-1]] = stack_dict[stack[-1]] - 1
        del stack[-1]
        n_ope += 1

    # 乗せるべきweightを求める
    weights_to_set = []
    for i in range(n_wei):
        weights_to_set += [i] * (weights[i] - stack_dict[i])
    # print(weights_to_set)

    for order in set(itertools.permutations(weights_to_set)):
        temp = dfs(idx_ex, order, stack, stack_dict, n_ope)
        ans = min(ans, temp)
    return ans


N = int(input())
for i_test in range(N):
    n_ex, n_wei = list(map(int, input().split()))

    if n_wei > 3:
        exit()
    
    stack = []
    stack_dict = {}
    for w in range(n_wei):
        stack_dict[w] = 0

    weights_require = []
    for i in range(n_ex):
        weights_require.append(list(map(int, input().split())))

    # 乗せるべきweightを求める
    weights_to_set = []
    idx_ex = 0
    weights = weights_require[idx_ex]
    for i in range(n_wei):
        weights_to_set += [i] * (weights[i] - stack_dict[i])

    ans = 99999
    for order in set(itertools.permutations(weights_to_set)):
        n_ope = 0
        temp = dfs(idx_ex, order, stack, stack_dict, n_ope)
        ans = min(ans, temp)

    print(f"Case #{i_test+1}: {ans}")


