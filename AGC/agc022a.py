s = input()

if len(s) < 26:
    # sに含まれていない文字の中で辞書順最小のものを付け加えれば良い
    for i in range(26):
        candi_ch = chr(ord('a') + i)
        if candi_ch not in s:
            print(s + candi_ch)
            exit()
else:
    for i in reversed(range(1, 26)):
        if s[i-1] < s[i]:
            s1 = s[0:i-1]
            for j in range(26):
                candi_ch = chr(ord('a') + j)
                if candi_ch > s[i-1] and candi_ch not in s1:
                    print(s1 + candi_ch)
                    exit()
    
    print(-1)
