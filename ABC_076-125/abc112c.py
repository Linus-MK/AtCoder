# 全探索
# といってもCx, Cy, Hを全部探索するとTLEになる。これは取りうるHの最大値が10^9程度であるからである。
# Cx, Cyは全通りやって、整合するHがあるか否か。

# 最初は、高さ0の情報は無意味だから無視しても良いというコードを書いていた。
# だけどそれだと1WAになる。in09で死ぬ。
# 入力を見てみよう。
# 5
# 32 67 0
# 32 68 1
# 33 68 0
# 31 68 0
# 32 69 0
# うん、そのとおりだわ。これは高さ0の情報がないと一意に確定できないわ。適当な推測をしてはいけないね。
# 高さ非0の情報を先に見て高さを確定させて、その後に高さ0の情報を見に行って整合性をチェックしよう。

n = int(input())

condition = []
for i in range(n):
    temp = list(map(int, input().split()))
    condition.append(temp)

codition = condition.sort(key=lambda x: x[2], reverse=True)  # 高さ非0の情報を先に見たいから

for x in range(0, 101):
    for y in range(0, 101):
        height_current = 0
        valid = True
        for cond in condition:
            if cond[2] == 0:
                height_temp = 0       + abs(x-cond[0]) + abs(y-cond[1])
                if height_current != 0 and height_current > height_temp:
                    valid = False
                    break

            else:
                height_temp = cond[2] + abs(x-cond[0]) + abs(y-cond[1])
                if height_current == 0:
                    height_current = height_temp
                elif height_temp != height_current:
                    # 不整合
                    valid = False
                    break
        
        if valid:
            print(f'{x} {y} {height_current}')
            exit()
