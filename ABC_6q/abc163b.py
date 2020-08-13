day, m = list(map(int, input().split()))
s = sum(map(int, input().split()))
if s > day:
    print(-1)
else:
    print(day - s)
