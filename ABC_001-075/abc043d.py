s = input()

if len(s) == 2:
    if s[0] == s[1]:
        print('1 2')
    else:
        print('-1 -1')
    exit()

for idx in range(len(s)-1):
    if s[idx] == s[idx+1]:
        print(f'{idx+1} {idx+2}')
        exit()

for idx in range(len(s)-2):
    if s[idx] == s[idx+2]:
        print(f'{idx+1} {idx+3}')
        exit()

print('-1 -1')
