h, w, m = list(map(int, input().split()))

objects = [list(map(int, input().split())) for _ in range(m)]

rows = [o[0]-1 for o in objects]
cols = [o[1]-1 for o in objects]
obj_dict = {(o[0]-1, o[1]-1): 1 for o in objects}

rows_appearance = [0] * h
for rr in rows:
    rows_appearance[rr] += 1

# print(rows_appearance)
m_row = max(rows_appearance)
m_row_num = 0
row_idx = []
for idx, rr in enumerate(rows_appearance):
    if rr == m_row:
        m_row_num += 1
        row_idx.append(idx)

cols_appearance = [0] * w
for cc in cols:
    cols_appearance[cc] += 1

# print(cols_appearance)
m_col = max(cols_appearance)
m_col_num = 0
col_idx = []
for idx, cc in enumerate(cols_appearance):
    if cc == m_col:
        m_col_num += 1
        col_idx.append(idx)

if m_row_num * m_col_num > m:
    # 鳩の巣原理。objectがないマスが必ずある。
    minus = 0
else:
    minus = 1
    for rr in row_idx:
        for cc in col_idx:
            if (rr, cc) not in obj_dict:
                # if rr, cc に対象物がなければ
                minus = 0
                break

print(m_col + m_row - minus)

# 解法メモ
# 基本的には、最大数の対象物がある行、列を狙えば良い。
# それで答えはいくつになる? 行と列の交点に対象物がある場合は、重複しているので1減る。
# 1減る場合と減らない場合なら、もちろん減らない場合のほうが良い。
# したがって、最大数となる行と列を全探索し、交点に対象物が全てあるか（行列の合計から1減る）、
# 対象物のない交点が存在するか（行列の合計が答え）を判定すれば良い。
# 最大数となる行と列を全探索するとTLEになる場合があるが、（大きな正方形の対角線上だけに対象物がある場合など）
# 対象物の数よりも「最大数となる行数×列数」が大きい場合は、鳩の巣原理より、対象物のない交点が存在する（行列の合計が答え）
# 対象物の最大数の制約より、間に合う。
