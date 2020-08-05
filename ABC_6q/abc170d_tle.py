# 回答例（TLE）
# 例えば2, 4, 6, 77, とあったとき、順に考えて4と6を除外した後に、77が該当するかどうかは 77 % 2だけ見れば良い。4や6の倍数ならば2の倍数なので。
# しかしこの考え方では計算量は減らない。
# a_iが 8*10**5 ~ 10*10**5 のような場合はどの要素も除外されないので、結局O(N^2)回の割り算をする必要があり、
# 計算量はO(N^2)、不適当

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

if n == 1:
    print(1)
    exit()

ans_list = []
temp = 0

for i in range(n):
    valid = True
    for div in ans_list:
        if nums[i] % div == 0:
            # 割り切れた
            valid = False
            break
        # if nums[i] < ans_list[j] * 2:
        #     break
    if valid:
        ans_list.append(nums[i])
        # ここで同じ数が2回以上出現する場合、 ans_listには入れるが（割る数のリストなので）最終的な個数からは除外しなければいけない
        if i < n-1 and nums[i] == nums[i+1]:
            temp += 1

    
ans = len(ans_list) - temp

print(ans)
# print(ans_list)
