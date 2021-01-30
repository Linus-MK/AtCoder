n, sec, damage = list(map(int, input().split()))

ans = 'No'
for i in range(n):
    x, y = list(map(int, input().split()))

    if x < sec and y > damage:
        ans = 'Yes'

print(ans) 
