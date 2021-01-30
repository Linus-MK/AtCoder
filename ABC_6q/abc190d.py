# 約数列挙
# ABC136Eより
def get_divisors(num):
    if num == 1:
        return [1]
    
    divisors = []
    for d in range(1, num):
        if d * d > num:
            break
        if num % d == 0: #約数
            divisors.append(d)
            if d * d != num:  # numの平方根の場合は重複するので追加しない
                divisors.append(int(num // d))

    return divisors

n = int(input())

divisors = get_divisors(2*n)
ans = 0
for p in divisors:
    if ((2 * n // p) - p + 1 ) % 2 == 0:
        ans += 1
print(ans)
