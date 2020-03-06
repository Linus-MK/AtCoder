n = input()
int_n = int(n)
# 解説通り

ans = int(n[0]) + 9 * (len(n) - 1)

for i in range(1, len(n)):
    if n[i] != '9':
        ans -= 1
        break
print(ans)
