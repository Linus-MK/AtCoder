s = input()
t = input()
ans = "No"
for i in range(26):
    s_slide = ""
    for char in s:
        char_idx = ord(char) - ord("a")
        char_idx = (char_idx + i) % 26
        new_char = chr(ord("a") + char_idx)
        s_slide += new_char
    if t == s_slide:
        ans = "Yes"
print(ans)
