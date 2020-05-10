n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

visited_city = {1: 0}
visited_city_inv = {0: 1}

now = 1
num = 0
while True:
    next_city = arr[now - 1]
    num += 1
    if next_city not in visited_city:
        visited_city[next_city] = num
        visited_city_inv[num] = next_city
        now = next_city
    else:
        break

if k < num:
    ans = visited_city_inv[k]
else:
    x = visited_city[next_city]
    period = num - x
    ans = visited_city_inv[x + (k - x) % period]

print(ans)
# print(visited_city)
