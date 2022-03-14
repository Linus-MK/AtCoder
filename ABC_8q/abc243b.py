n = int(input())
a_lis = list(map(int, input().split()))
b_lis = list(map(int, input().split()))

hit = 0
for i in range(n):
    if a_lis[i] == b_lis[i]:
        hit += 1

hit_or_blow = len(set(a_lis) & set(b_lis))
print(hit)
print(hit_or_blow - hit)
