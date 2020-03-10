# 全探索で十分間に合う

eight, ten = list(map(int, input().split()))
for i in range(1000+5):
    if eight == int(i * 0.08) and ten == int(i * 0.1):
        print(i)
        exit()

print(-1)
