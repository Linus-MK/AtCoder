n = int(input())
boss = list(map(int, input().split()))

subordinate = {}
for b in boss:
    subordinate[b] = subordinate.get(b, 0) + 1

for i in range(1, n+1):
    print(subordinate.get(i, 0))

# 公式解答はsubordinateを辞書ではなくリストで持っている。まぁ最後にどうせキーに対応する値があるか無いか調べるので、リストでも良いか。
# 最初に全部0にするから欠損値も気にしなくてよいし。
