n = int(input())

d = dict()
for i in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1

max_vote = 0
for k, v in d.items():
    if v > max_vote:
        max_vote = v
        ans = k

print(ans)
