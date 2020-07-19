n = int(input())

ans = n // 500 * 1000
n = n % 500
ans += n // 5 * 5

print(ans)
