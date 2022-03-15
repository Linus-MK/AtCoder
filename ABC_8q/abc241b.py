n, m = list(map(int, input().split()))
a_lis = list(map(int, input().split()))
b_lis = list(map(int, input().split()))

a_dict = {}
for a in a_lis:
    a_dict[a] = a_dict.get(a, 0) + 1

b_dict = {}
for b in b_lis:
    b_dict[b] = b_dict.get(b, 0) + 1

ans = 'Yes'
for key in b_dict.keys():
    if b_dict[key] > a_dict.get(key, 0):
        ans = 'No'

print(ans)
