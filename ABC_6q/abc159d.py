n = int(input())
nums = list(map(int, input().split()))

mydict = {}

for num in nums:
    if not num in mydict:
        mydict[num] = 1
    else:
        mydict[num] += 1

# print(mydict)

all_sum = 0
for key, value in mydict.items():
    all_sum += value * (value - 1)// 2

for num in nums:
    print(all_sum - (mydict[num] - 1))
