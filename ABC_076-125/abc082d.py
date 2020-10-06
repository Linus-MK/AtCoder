# 
# セグメント木の問題（蟻本p.156） と少し似ていたので、
# やや分かりにくいが、これは縦横分離できる問題である。
# ある地点までのTの個数の偶奇を見ると、進むのがx軸（横）方向かy軸（縦）方向かが確定する。
# 最初は正方向で、それ以外のFの塊は正負を自由に選べる。
# あとは縦横独立に、目標の座標に到達できるかを考えれば良い。
# 全通りを総当たりで考える→×（TLE）
# DP。直前の座標からa進むかa戻るかの動きをしたものが、次の到達可能点になる。

# PyPyでACにはなるが、appendで配列を順次追加するのはTLEになりやすいので避けるべき。最初に2次元配列を作るのが良い

s = input()
s = s + '-'  # ループ最後の処理を簡単にするための番兵
forward = s.count('F')

x = [[False] * (forward*2+1)]
y = [[False] * (forward*2+1)]

x[0][forward] = True
y[0][forward] = True

direction = 0  # 0がx、1がy
count_len = 0
first = True # 最初はx軸正の方向
for char in s:
    if char == 'F':
        count_len += 1
    else:
        if first:
            x.append([False] * (forward*2+1))
            x[-1][forward + count_len] = True
            first = False

        elif direction == 0:
            x.append([False] * (forward*2+1))
            for pos in range(forward*2+1):
                if (0 <= pos-count_len and x[-2][pos-count_len] == True) or \
                    (pos+count_len <= forward*2 and  x[-2][pos+count_len] == True):
                    x[-1][pos] = True
        else:
            y.append([False] * (forward*2+1))
            for pos in range(forward*2+1):
                if (0 <= pos-count_len and y[-2][pos-count_len] == True) or \
                    (pos+count_len <= forward*2 and y[-2][pos+count_len] == True):
                    y[-1][pos] = True
        
        if char == 'T':
            direction = 1 - direction  # 方向転換
        
        count_len = 0

xx, yy = list(map(int, input().split()))
if 0 <=forward+xx <= forward*2 and x[-1][forward+xx] and 0 <=forward+yy <= forward*2 and y[-1][forward+yy]:
    print('Yes')
else:
    print('No')
