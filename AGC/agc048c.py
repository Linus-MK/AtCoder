n, length = list(map(int, input().split()))

start = list(map(int, input().split()))
end = list(map(int, input().split()))

# 全てのkに対して
# Bk = Ak or Bk = A(k+1)-1 or Bk = A(x-1)+1 or ……
# 4 11
# 3 4 6 10
# 1 5 6 11
#  3から行けるのは、左端の0+1=1、3+-0=3(もともと), 4-1=3, 6-2=4, 10-3=7, 右端11-3=8 (12-4とみなすとうまくいくかも)
# 10から行けるのは、左端の0+4=4, 3+3=6, 4+2=6, 6+1=7, 10+-0=10(もともと), 右端12-1=11
# いや上2行って定数（3）の差しかないわ。
# これを1つ1つ見ていくとダメ。O(N^2)になってしまう!
# →二分探索なら行けそう
# kが変わると行ける座標も変わってしまうので、探索点を上手く取って差分を吸収する

valid_dest = [0] + start.copy() + [length+1]
for i in range(len(valid_dest)):
    valid_dest[i] -= (i-1)
# print(valid_dest)

# 不要
# valid_left = [0] + start.copy() + [length+1]
# for i in range(len(valid_left)):
#     valid_left[i] += (n-i)
# print(valid_left)

import bisect
ans = 0
prev_dest_idx = -1
for idx, dest in enumerate(end):
    dest_idx = bisect.bisect_left(valid_dest, dest - idx)
    if dest_idx < len(valid_dest) and valid_dest[dest_idx] == dest - idx:
        # print(idx+1, dest_idx)
        # 回数計算
        if dest == start[idx]:
            pass
        elif idx > 0 and dest - end[idx-1] == 1:
            if dest < start[idx]:
                ans += 1
            elif dest > start[idx]:
                pass
        # elif idx < n-1 and end[idx+1] - dest == 1:
        #     ans += 1
        else:
            ans += abs(dest_idx - (idx+1))
        # print(ans)

        prev_dest_idx = dest_idx
    else:
        # 到達不能
        print(-1)
        exit()
print(ans)
