a,b,m =  list(map(int, input().split()))

a_price =  list(map(int, input().split()))
b_price =  list(map(int, input().split()))

waribiki = [list(map(int, input().split())) for _ in range(m)]

ans = min(a_price) + min(b_price)

for i in waribiki:
    temp = a_price[i[0]-1] + b_price[i[1]-1] - i[2]
    if temp < ans:
        ans = temp

print(ans)