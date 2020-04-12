def is_prime(num):
    if num == 1:
        raise ValueError("error!")
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True
    
n, k = list(map(int, input().split()))
mod = 10 ** 9 + 7

n_power_table = [-1] * (k+1)
for i in range(k):
    n_power_table[i] = pow(i, n, mod)

# 素数リストを作っておく
prime_list = []
for i in range(2, k+1):
    if is_prime(i):
        prime_list.append(i)

prime_2_list = []
prime_3_list = []
prime_4_list = []
prime_5_list = []

ll = len(prime_list)
for i, p1 in enumerate(prime_list):
    for j in range(i+1, ll):
        p2 = prime_list[j]
        if p1*p2 > k:
            break
        prime_2_list.append(p1*p2)
        for v in range(j+1, ll):
            p3 = prime_list[v]
            if p1*p2*p3 > k:
                break
            prime_3_list.append(p1*p2*p3)
            # print(p1, p2, p3)
            for w in range(v+1, ll):#enumerate(prime_list[v+1:]):
                p4 = prime_list[w]
                if p1*p2*p3*p4 > k:
                    break
                prime_4_list.append(p1*p2*p3*p4)
                for x in range(w+1, ll):#, p5 in enumerate(prime_list[w+1:]):
                    p5 = prime_list[x]
                    if p1*p2*p3*p4*p5 > k:
                        break
                    prime_5_list.append(p1*p2*p3*p4*p5)

prime_2_list.sort()
prime_3_list.sort()
prime_4_list.sort()
prime_5_list.sort()

# prime_3_list = []
# for i, p1 in enumerate(prime_list):
#     for j, p1_ in enumerate(prime_2_list):
#         if p1*p1_ > k:
#             break
#         prime_3_list.append(p1*p1_)

# list(set(prime_3_list)).sort()

# print(prime_3_list)

ans = 0
temp = 0

for g in range(1, k+1):
    # kosuu は、gcd = gとなる組み合わせの個数
    p = k // g
    
    kosuu = pow(p, n, mod)

    for prime in prime_list:
        if prime > p:
            break
        kosuu -= n_power_table[p//prime]
    
    for prime in prime_2_list:
        if prime > p:
            break
        kosuu += n_power_table[p//prime]
    
    for prime in prime_3_list:
        if prime > p:
            break
        kosuu -= n_power_table[p//prime]

    for prime in prime_4_list:
        if prime > p:
            break
        kosuu += n_power_table[p//prime]

    for prime in prime_5_list:
        if prime > p:
            break
        kosuu -= n_power_table[p//prime]

    kosuu %= mod
    ans += g * kosuu
    # print(g, kosuu)
    temp += kosuu

print(ans% mod)
# print(temp)
