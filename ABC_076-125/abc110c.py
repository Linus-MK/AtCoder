s = input()
t = input()

s_arr = [0] * 26
t_arr = [0] * 26
for i in range(len(s)):
    temp = ord(s[i]) - ord('a')
    s_arr[temp] += 1
    temp = ord(t[i]) - ord('a')
    t_arr[temp] += 1

s_arr.sort()
t_arr.sort()

ans = 'Yes'
for i in range(26):
    if s_arr[i] != t_arr[i]:
        ans = 'No'

print(ans)
