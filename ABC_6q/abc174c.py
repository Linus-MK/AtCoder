n = int(input())

now_mod = 0

if n % 2 == 0:
    print(-1)
    exit()

for i in range(1, n+1):
    now_mod *= 10
    now_mod += 7
    now_mod %= n
    if now_mod == 0:
        print(i)
        exit()

print(-1)
exit()
