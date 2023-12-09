# 上から流れ込んでくるやつ。頂点1を根とする木になる。
# 多分、ノード1からの距離が遠いところから見て行って、最初に勝敗が付いたところの符号。未証明だけど。

n = int(input())
nums = list(map(int, input().split()))
edges = list(map(int, input().split()))

distance = [-1] * n
distance[0] = 0

for i, e in enumerate(edges):
    parent = e - 1
    child = i + 1
    distance[child] = distance[parent] + 1

# print(distance)

distance_gotono_strength = dict()

max_distance = 0
for i in range(n):
    dist = distance[i]
    distance_gotono_strength[dist] = distance_gotono_strength.get(dist, 0) + nums[i]

    max_distance = max(dist, max_distance)

# print(max_distance)
# print(distance_gotono_strength)

for dist in range(max_distance, -1, -1):
    strength = distance_gotono_strength[dist]
    if strength > 0:
        print("+")
        exit()
    elif strength < 0:
        print("-")
        exit()

print("0")