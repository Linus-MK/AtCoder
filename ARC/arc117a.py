a, b = list(map(int, input().split()))

s = 10 ** 8
ans = []
ans += range(1, a)
ans.append(s - a*(a-1)//2)
ans += range(-b+1, 0)
ans.append(-s + b*(b-1)//2)

ans_str = map(str, ans)
print(' '.join(ans_str))
