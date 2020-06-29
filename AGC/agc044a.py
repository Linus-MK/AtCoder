# 解説PDF読んで解説放送見てAC

# 逆から操作を考える（終点のNから考える）
# スカスカDP。なので配列を作らずに辞書で管理する必要がある

def calc_cost(n, ans_dict):

    min_cost = n * d

    inc_2 = (n + 2 - 1) // 2
    if inc_2 not in ans_dict:
        ans_dict[inc_2] = calc_cost(inc_2, ans_dict)
    min_cost = min(min_cost, d * (inc_2 * 2 - n) + a + ans_dict[inc_2])

    dec_2 = n // 2
    if dec_2 not in ans_dict:
        ans_dict[dec_2] = calc_cost(dec_2, ans_dict)
    min_cost = min(min_cost, d * (- dec_2 * 2 + n) + a + ans_dict[dec_2])

    inc_3 = (n + 3 - 1) // 3
    if inc_3 not in ans_dict:
        ans_dict[inc_3] = calc_cost(inc_3, ans_dict)
    min_cost = min(min_cost, d * (inc_3 * 3 - n) + b + ans_dict[inc_3])

    dec_3 = n // 3
    if dec_3 not in ans_dict:
        ans_dict[dec_3] = calc_cost(dec_3, ans_dict)
    min_cost = min(min_cost, d * (- dec_3 * 3 + n) + b + ans_dict[dec_3])

    inc_5 = (n + 5 - 1) // 5
    if inc_5 not in ans_dict:
        ans_dict[inc_5] = calc_cost(inc_5, ans_dict)
    min_cost = min(min_cost, d * (inc_5 * 5 - n) + c + ans_dict[inc_5])

    dec_5 = n // 5
    if dec_5 not in ans_dict:
        ans_dict[dec_5] = calc_cost(dec_5, ans_dict)
    min_cost = min(min_cost, d * (- dec_5 * 5 + n) + c + ans_dict[dec_5])

    ans_dict[n] = min_cost
    return min_cost

n_testcase = int(input())
for i in range(n_testcase):
    n, a, b, c, d = list(map(int, input().split()))

    # テストケースごとに辞書はリセットしないとダメですね
    ans_dict = {}

    ans_dict[0] = 0
    ans_dict[1] = d  # 1減らすのが常に最善

    ans = calc_cost(n, ans_dict)
    print(ans)
    # print(ans_dict)
