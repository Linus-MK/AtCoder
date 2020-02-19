num = list(input())
num = list(map(int, num))
length = len(num)

ans = 0

# isspecial = True
# # 9が１子以上続いたあとに5
# if num[-1] == 5:
#     for i in reversed(range(length - 1)):
#         if num[i] != 9:
#             isspecial = False
#             break
# else:
#     isspecial = False
# if isspecial:
#     print(6)
#     exit()    

for i in reversed(range(1, length)):
    digit = num[i]
    if digit < 5:
        ans += digit
    elif i > 0 and digit == 5 and num[i-1] < 5:
        ans += digit
    else:
        ans += (10 - digit)
        if i > 0:
            num[i-1] += 1
        else:
            ans += 1

digit = num[0]
if digit <= 5:
    ans += digit
else:
    ans += (11 - digit)

print(ans)
