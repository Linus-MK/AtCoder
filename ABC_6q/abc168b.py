k = int(input())
s = input()
print(s[:k] + ('...' if len(s) > k else ''))
# s[:k]はk文字未満のときもエラーが発生しない。
