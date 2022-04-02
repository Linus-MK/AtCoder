n= int(input())
nums = list(map(int, input().split()))

area_list = set()

for a in range(1, 200):
    for b in range(a, 200):
        area_list.add(4*a*b + 3*a + 3*b)

ans = 0
for num in nums:
    if num not in area_list:
        ans += 1
print(ans)
