import random
random.seed(0)

sr, sc, tr, tc, prob = input().split()
sr = int(sr)
sc = int(sc)
tr = int(tr)
tc = int(tc)
hori_wall = []
for i in range(20):
    hori_wall.append(input())

vart_wall = []
for i in range(19):
    vart_wall.append(input())

ans = 'DR' * 60
# 進めなくなったときに脱出
for i in range(1, 7):
    # ans[i*8] = 'U'  # Dの代わりにU
    # ans[i*8 + 5] = 'L'  # Rの代わりにL
    ans = ans[:i*16 - 1] + 'U' + ans[i*16:]  # Dの代わりにU
    ans = ans[:i*16 + 6] + 'L' + ans[i*16 + 7:] # Rの代わりにL

# ゴールが右下マスの真上もしくは真左だった場合は、その方向に進む
if tr == 19:
    # 真左
    ans += 'L' * 20
elif tc == 19:
    # 真上
    ans = 'U' * 20
else:
    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[3, 3, 1, 1], k=20)
    ans += ''.join(ch_list)
    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[1, 1, 3, 3], k=20)
    ans += ''.join(ch_list)
    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[3, 3, 1, 1], k=20)
    ans += ''.join(ch_list)
    ch_list = random.choices(['U', 'L', 'R', 'D'], weights=[1, 1, 3, 3], k=20)
    ans += ''.join(ch_list)
print(ans)
