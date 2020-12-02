a, b, x, y = list(map(int, input().split()))

ans = 10**10

temp = x*abs((b-a)*2+1) # 廊下だけ
ans = min(temp, ans)
temp = y*(abs((b-a)*2+1)//2) + x
ans = min(temp, ans)

print(ans)
