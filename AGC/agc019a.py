a, b, c, d = list(map(int, input().split()))
n = int(input())

# 1リットル買う
min_for_one = min(a*4, b*2, c)

min_for_two = min(a*8, b*4, c*2, d)

if n % 2 == 1:
    print((n //2)* min_for_two + min_for_one)
else:
    print(n // 2 * min_for_two)
