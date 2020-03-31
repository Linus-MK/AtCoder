n, m = list(map(int, input().split()))

query = []
for i in range(m):
    query.append(list(map(int, input().split())))

for num in range(1000):
    flag = True
    s_num = str(num)
    if len(s_num) != n:
        continue  # ここがflag=Falseだと、下で配列の範囲外参照になってエラー
    for j in query:
        if s_num[j[0]-1] != str(j[1]):
            flag = False
    if flag:
        print(num)
        exit()

print(-1)
