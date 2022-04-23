import string
s = input()
ans = "No"
if len(set(s)) == len(s):
    lower = 0
    upper = 0
    for let in s:
        if let in string.ascii_lowercase:
            lower += 1
        else:
            upper += 1
    if lower > 0 and upper > 0:
        ans = "Yes"

print(ans)
