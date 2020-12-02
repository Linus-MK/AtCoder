# 自分の解法は現在状態（のうち消去しうるところ）を記憶しておく、オートマトンっぽい解法。
# コンテスト終了後にみんなstackって言っててびっくりした。
# 先頭からstackに積んでいって、foxができたら削除する、を繰り返せばよい。

n = int(input())
s = input()

status = [-1]
n_del = 0
for char in s:
    if char == 'f':
        status.append(1)
    elif char == 'o':
        if status[-1] == 1:
            status[-1] = 2
        else:
            status = [-1]
    elif char == 'x':
        if status[-1] == 2:
            del status[-1]
            n_del += 1
        else:
            status = [-1]

    else:
        status = [-1]

print(n - n_del * 3)
