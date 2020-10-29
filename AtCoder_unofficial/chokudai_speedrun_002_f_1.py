# setに入れてしまってその長さとかで解けないかな?
# setやlistはsetに入れられない。tupleなら可能

# Python (3.8.2)で510ms, PyPy3 (7.3.0)で398msでした。ACできた。

n = int(input())
ans = set()
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a < b:
        a, b = b, a
    ans.add((a, b))
print(len(ans))
