length, layer = list(map(int, input().split()))
hands = input()

start = hands * 2

for i in range(layer):
    end = []  # 文字列の変更はできないのでリストで捌く
    for idx in range(length):
        first = start[idx*2]
        second = start[idx*2+1]
        if first == second:
            winner = first
        elif (first, second) == ('R', 'S') or (first, second) == ('S', 'R'):
            winner = 'R'
        elif (first, second) == ('P', 'S') or (first, second) == ('S', 'P'):
            winner = 'S'
        elif (first, second) == ('R', 'P') or (first, second) == ('P', 'R'):
            winner = 'P'
        else:
            raise #エラー
        end.append(winner)
    
    start = ''.join(end)
    start *= 2

print(start[0])
