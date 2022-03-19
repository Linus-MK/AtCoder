l, r = list(map(int, input().split()))
s = input()

ans = s[:l-1] + ''.join(reversed(s[l-1:r])) + s[r:]
print(ans)
