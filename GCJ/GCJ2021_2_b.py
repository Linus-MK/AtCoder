# 約数・倍数の関係にある列の最長数
# 最初の数は2にできないことに注意
# 
# 3, 6, 24 が条件を満たすとき、後ろ2つを足し合わせた
# 3, 30 も条件を満たす。

# dp2[n] := 初項2以上で、和がnとなる数列のうち、最長の長さ
# dp3[n] := 初項3以上で、和がnとなる数列のうち、最長の長さ
# と定義する。
# 答えは dp3[n]である。
# dp2: https://oeis.org/A167866


# 約数列挙
# 再帰にするぞ

def get_divisors(num):
    if num == 1:
        return set([1])
    
    divisors = set()
    for d in range(2, num+1):
        if d * d > num:
            return set([1, num])
        if num % d == 0: #約数
            divisors = get_divisors(num // d)

            # print(divisors)

            temp_set = set()
            for base in divisors:
                temp_set.add(base * d)
            # print('temp:', temp_set)
            divisors = divisors | temp_set
            break

            # divisors.append(d)
            # if d * d != num:  # numの平方根の場合は重複するので追加しない
            #     divisors.append(int(num // d))

    return divisors

# print(get_divisors(30))
# exit()

N = int(input())

nums = []
for i_test in range(N):
    num = int(input())
    nums.append(num)

max_num = max(nums)+10
# max_num = 100

dp2 = [0] * (max_num)

for num in range(2, max_num):
    divisors = get_divisors(num)
    # print(num, divisors)
    for div in divisors:
        if div == 1:
            continue
        temp = 1 + dp2[(num//div)-1]
        if temp > dp2[num]:
            dp2[num] = temp

# print(dp2)

for i_test in range(N):
    num =nums[i_test]
    
    divisors = get_divisors(num)
    
    ans = 1
    for div in divisors:
        if div <= 2:
            continue
        temp = 1 + dp2[(num//div)-1]
        if temp > ans:
            ans = temp

    print("Case #{0}: {1}".format(i_test+1, ans))
