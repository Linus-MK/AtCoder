s = input()
repeat_num = int(input())

count = 1
count_list = []
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        count_list.append(count)
        count = 1

count_list.append(count)

if len(count_list) == 1:
    print((len(s) * repeat_num ) // 2)
else:
    if s[0] != s[-1]:
        single = sum(list(map(lambda x: x//2, count_list)))
        print(single * repeat_num)
    else:
        # s[0] == s[-1] 繰り返しによってつながる
        single = sum(list(map(lambda x: x//2, count_list[1:-1])))
        print(single * repeat_num
            + (count_list[0]) // 2
            + (count_list[-1]) // 2
            + (count_list[0] + count_list[-1]) // 2 * (repeat_num - 1))
