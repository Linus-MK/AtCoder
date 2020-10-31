a, b, c = list(map(int, input().split()))
ans = 1
ans *= a*(a+1)//2
ans *= b*(b+1)//2
ans *= c*(c+1)//2
print(ans%998244353)