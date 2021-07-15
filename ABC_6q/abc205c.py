a, b, c = list(map(int, input().split()))

c = c % 2
if c == 0:
    c = 2
if pow(a, c) > pow(b, c):
    print('>')
elif pow(a, c) == pow(b, c):
    print('=')
else:
    print('<')
