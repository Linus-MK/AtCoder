# 1回の操作をするたびに、求める量は-1倍になるので
a, b, c, k = list(map(int, input().split()))
if k % 2 == 1:
    print(b-a)
else:
    print(a-b)
