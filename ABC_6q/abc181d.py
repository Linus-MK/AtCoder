s = input()

if len(s) == 1:
    if s == '8':
        print('Yes')
    else:
        print('No')
    exit()

if s == 2:
    if int(s) % 8 == 0:
        print('Yes')
    elif int(s[0]+s[1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
# print(freq)

for i in range(125):
    str_i_8 = f'{i*8:03}'
    if '0' in str_i_8:
        continue

    freq_i8 = {}
    for ch in str_i_8:
        freq_i8[ch] = freq_i8.get(ch, 0) + 1
    
    valid = True
    for k in freq_i8:
        if freq.get(k, 0) < freq_i8.get(k):
            valid = False
    if valid:
        print('Yes')
        exit()

print('No')
