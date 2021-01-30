a, b, c = list(map(int, input().split()))

if (c == 0 and a > b) or (c == 1 and a >= b):
    print('Takahashi')
else:
    print('Aoki')
    