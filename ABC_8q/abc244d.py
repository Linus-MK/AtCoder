start = input().split()
end = input().split()

ans = "Yes"
if start[0] == end[1] and start[1] == end[0]:
    ans = "No"
if start[1] == end[2] and start[2] == end[1]:
    ans = "No"
if start[0] == end[2] and start[2] == end[0]:
    ans = "No"
print(ans)
