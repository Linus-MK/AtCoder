# 少数の人間だけが正解することがあるからdictで管理するかと思ったけど、結局全員に対して0で初期化しているので
# dictの利点は無い。listでも良かったね。
n, k, q = list(map(int, input().split()))

correct = {}
for parti in range(1, n+1):
    correct[parti] = 0

for i in range(q):
    a = int(input())
    correct[a] += 1

for parti in range(1, n+1):
    if k - q + correct[parti] > 0:
        print("Yes")
    else:
        print("No")
