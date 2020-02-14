n = int(input())
nums = list(map(int, input().split()))

print('NO' if (sum(map(lambda x:x%2, nums)))%2 else 'YES')
# 奇数の数が奇数個ならNO、偶数個ならYES を1行で書いてみた
