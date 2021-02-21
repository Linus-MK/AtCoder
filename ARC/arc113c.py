s = input()
le = len(s)

appearance = []
current_char = ''
minus = 0

i = 0
while i < le:
    if (i <= le - 3) and s[i] == s[i+1] != s[i+2]:
        current_char = s[i]
        temp = (i+1, s[i])
        appearance.append(temp)
        # print(i+1)
        i += 2
    else:
        if s[i] == current_char:
            minus += 1
        i += 1

ans = 0
pos_prev = le # 大丈夫か？
char_prev = ''

for ap in reversed(appearance):
    char = ap[1]
    pos = ap[0]
    if char == char_prev:
        ans += (pos_prev - pos - 2)
    else:
        ans += (le - pos - 1)
    char_prev = char
    pos_prev = pos

print(ans- minus)
