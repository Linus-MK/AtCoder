n, m, t = list(map(int, input().split()))

present_battery = n
end_prev = 0
ans = 'Yes'
for i in range(m):
    start, end = list(map(int, input().split()))

    present_battery -= (start - end_prev)
    if present_battery <= 0:
        ans = 'No'
    present_battery += (end - start)
    present_battery = min(present_battery, n)

    end_prev = end

present_battery -= (t - end_prev)
if present_battery <= 0:
    ans = 'No'
    
print(ans)
