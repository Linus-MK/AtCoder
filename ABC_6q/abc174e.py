n, k = list(map(int, input().split()))

lengths = list(map(int, input().split()))


def is_valid(unit):
    # k回以下の切断で実現可能か

    n_cut = sum(map(lambda p: (p+unit-1) // unit - 1, lengths))
    # print(unit, n_cut)
    
    return n_cut <= k


unit_ok = 10 ** 9 + 1
unit_ng = 0

# めぐる式二分探索
while abs(unit_ok - unit_ng) > 1:
    mid = (unit_ok + unit_ng) // 2
    if is_valid(mid):
        unit_ok = mid
    else:
        unit_ng = mid

print(unit_ok)
