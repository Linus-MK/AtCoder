# 3 3 1 1

# 100
# 010
# 001

# 3 3 1 0

# 100
# 100
# 100

# 4 4 2 1
# 1100
# 1100
# 1100
# 0011

# 4 3 1 1

# 1000
# 1000
# 0111

# ……あ。全部0→左側A列を逆転させる→下側B列を逆転させる　で構成可能だ。

h, w, a, b = list(map(int, input().split()))

for _ in range(h-b):
    print('1'*a + '0'*(w-a))
for _ in range(b):
    print('0'*a + '1'*(w-a))