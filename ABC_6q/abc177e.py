import math
n = int(input())
nums = list(map(int, input().split()))

gcd_ = nums[0]
for num in nums[1:]:
    gcd_ = math.gcd(gcd_, num)

if gcd_ >= 2:
    print('not coprime')
    exit()

def smallest_divisor(num, start):
    if num == 1:
        raise ValueError("error!")
    d = start
    while d * d <= num:
        if num % d == 0:
            return d
        d += 1
    return num


prime_set = set()

for num in nums:
    if num == 1:
        continue

    soinsuu = set()
    
    warareru = num
    start = 2
    while True:
        divi = smallest_divisor(warareru, start)
        soinsuu.add(divi)
        warareru = warareru // divi
        start = divi
        if warareru == 1:
            break
    # print(soinsuu)
    if soinsuu & prime_set:
        print('setwise coprime')
        exit()
    else:
        prime_set |= soinsuu

print('pairwise coprime')
