n = int(input())
names = []
for i in range(n):
    names.append(input().split())
# ある人の姓名のどちらを選ぶか は、他の人のあだ名が使用可能か に影響しないことに注意。順に調べれば良い。

for i_name in range(n):
    ok = [True, True]
    for pos in range(2):
        candi = names[i_name][pos]
        for j_name in range(n):
            if i_name == j_name:
                continue
            for pos2 in range(2):
                if candi == names[j_name][pos2]:
                    ok[pos] = False
        
    if ok[0] == ok[1] == False:
        print("No")
        exit()

print("Yes")
