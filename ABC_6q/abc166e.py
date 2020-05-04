n = int(input())

ai = list(map(int, input().split())) 

bi = [0] * n
ci = [0] * n

for i, aa in enumerate(ai):
    bi[i] = aa + i
    ci[i] = aa - i

# print(bi)

bi_dict = {}
ci_dict = {}
for i in range(n):
    bi_dict[bi[i]] = bi_dict.get(bi[i], 0) + 1
    ci_dict[ci[i]] = ci_dict.get(ci[i], 0) + 1

ans = 0
for b in bi_dict:
    ans += bi_dict[b] * ci_dict.get(-b, 0)
print(ans)
