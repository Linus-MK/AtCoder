n = int(input())

all_change_depth = 0
required_depth = []

change_posi_zero = []
change_nega = []

for i in range(n):
    paren = input()
    current_depth = 0
    min_depth = 0
    for ch in paren:
        if ch == '(':
            current_depth += 1
        else:
            current_depth -= 1
            min_depth = min(min_depth, current_depth)

    all_change_depth += current_depth
    if current_depth >= 0:
        change_posi_zero.append( (current_depth, -(min_depth)) )
    else:
        change_nega.append( (current_depth, -(min_depth)) )

# まず変化depthの合計が非ゼロならNo。（と）の個数が全体で不一致なので。
if all_change_depth != 0:
    print('No')
    exit()

# 変化depthが0と正の要素を、要求depthが小さい順に投入する。
# 現在depth < 要求depthならアウト
current_depth = 0
change_posi_zero.sort(key=lambda x: x[1])
for paren in change_posi_zero:
    change_depth = paren[0]
    required_depth = paren[1]

    if required_depth > current_depth:
        print('No')
        exit()
    current_depth += change_depth

# 変化depthが負の要素を、要求depthが大きい順に投入する。
# 現在depth < 要求depthならアウト
change_nega.sort(key=lambda x: x[1], reverse=True)

for paren in change_nega:
    change_depth = paren[0]
    required_depth = paren[1]

    if required_depth > current_depth:
        print('No')
        exit()
    current_depth += change_depth

assert(current_depth == 0)
print('Yes')
