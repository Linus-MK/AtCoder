# 構成系、構築系
# コーナーケースあり

n, m = list(map(int, input().split()))

if m < 0:
    print(-1)
    exit()
if m == n:
    print(-1)
    exit()
if n > 1 and m == n-1:
    print(-1)
    exit()

for i in range(1, n):
    start = 10*i + 5
    end = 10*i + 6
    print(f'{start} {end}')

start = 10* (n-1 - m)+1
end = 10 ** 9
print(f'{start} {end}')

# 区間スケジューリング問題であり、高橋くんのアルゴリズムが最適解になるので、
# 高橋 >= 青木 が必ず成り立つ。
# 条件を満たすように適宜構成すれば良い。
# n=1, m=0を見逃して1回WAした
