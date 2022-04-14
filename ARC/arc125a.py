n, m = list(map(int, input().split()))
start = list(map(int, input().split()))
end = list(map(int, input().split()))

# 不可能判定
if max(start) == min(start):
    only = start[0]
    for e in end:
        if e != only:
            print(-1)
            exit()
    
    print(m)
    exit()

init = start[0]
for i, num in enumerate(start):
    if init != num:
        temp_forward = i
        break

for i in range(n-1, -1, -1):
    if init != start[i]:
        temp_back = n - i
        break

prev = init
count = 0
for i in range(m):
    if end[i] != prev:
        count += 1
    prev = end[i]

if count >= 1:
    ans = m + count-1 + min(temp_forward, temp_back)
else:
    ans = m
print(ans)
