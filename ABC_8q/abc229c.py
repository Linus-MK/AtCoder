n, weight = list(map(int, input().split()))
cheese = []
for i in range(n):
    a, b = list(map(int, input().split()))
    cheese.append([a, b])

cheese.sort(key=lambda s: s[0], reverse=True)
w_rest = weight
deli = 0
for i in range(n):
    current = cheese[i]

    use = min(current[1], w_rest)
    w_rest -= use
    deli += use * current[0]
    if w_rest == 0:
        break

print(deli)
