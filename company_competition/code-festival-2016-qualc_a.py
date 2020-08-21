s = input()

pos_c = s.find('C')
if pos_c >= 0 and s[pos_c:].find('F') >= 0:
    print('Yes')
else:
    print('No')
