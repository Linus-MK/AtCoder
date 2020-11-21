summ, prod = list(map(int, input().split()))

for d in range(1, prod+1):
    if d * d > prod:
        break
    if prod % d == 0: #約数
        sum2 = d + prod // d
        if summ == sum2 :
            print('Yes')
            exit()

print('No')
