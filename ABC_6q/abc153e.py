# pythonでTLE，pypyで通した

h, n = list(map(int, input().split()))

hp_and_magic = [list(map(int, input().split())) for _ in range(n)]

arr = [10 ** 9] * (h+1)
# arr[k] := hpがkの敵を倒すのに必要な最小魔力
arr[0] = 0
arr[1] = min([ele[1] for ele in hp_and_magic])

for i in range(2, h+1):
    # arr[i] = 10 ** 9
    for ele in hp_and_magic:
        if i-ele[0] >= 0:
            arr[i] = min(arr[i], arr[i-ele[0]] + ele[1])
        else:
            arr[i] = min(arr[i], ele[1])

print(arr[h])