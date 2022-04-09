# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1


N = int(input())
for i_test in range(N):
    # 差が2のべき乗になるようなペアを用意する
    # 10^9 < 2^30 より、2^0〜29の30ペアを作る

    li = []
    small_list = []
    large_list = []
    current_small = 1
    for i in range(30):
        diff = 2 ** i
        while current_small in li:
            current_small += 1
        small = current_small
        large = current_small + diff
        li.append(small)
        li.append(large)
        small_list.append(small)
        large_list.append(large)

    # print(sum(large_list) - sum(small_list)) 1073741823 = 2^30 - 1
    # あと20ペアで合計を調整する。後段の交換には使用しない
    extra_list = []
    extra_list.append([10**9, 100])
    extra_list.append([73741823 + 101 + 100, 101])
    # これで合計が釣りあったので、あと18ペアは合計が同じでありさえすればよい。
    for i in range(18):
        if i % 2 == 1:
            extra_list.append([10000 + i * 2, 10000 + i * 2 + 1])
        else:
            extra_list.append([10000 + i * 2 + 1, 10000 + i * 2])

    for i in range(20):
        small = extra_list[i][0]
        large = extra_list[i][1]
        li.append(small)
        li.append(large)
        small_list.append(small)
        large_list.append(large)

    # print(sum(large_list) - sum(small_list))
    # print(li)
    # print(len(li))
    # print(len(set(li)))
    first_sum = sum(li)

    # ここで数字を読む
    n = int(input())
    if n != 100:
        exit()

    ans_str = map(str, li)
    ans_joined = " ".join(ans_str)
    print(ans_joined, flush=True)

    nums = list(map(int, input().split()))
    if nums[0] < 0:
        # エラー
        exit()
    nums.sort()
    new_small = nums[0::2]
    new_large = nums[1::2]
    diff = sum(new_large) - sum(new_small)
    second_sum = sum(nums)
    assert diff % 2 == 0

    x = diff // 2
    bit_idx = 0
    ans = []
    for bit_idx in range(30):
        if x % 2 == 1:
            # 2 ** bit_idx を入れ替える
            ans.append(large_list[bit_idx])
        else:
            ans.append(small_list[bit_idx])
        x = x // 2
    for i in range(30, 50):
        ans.append(small_list[i])

    ans = ans + new_small

    ans_str = map(str, ans)
    ans_joined = " ".join(ans_str)
    print(ans_joined, flush=True)
    # print(sum(ans), (first_sum + second_sum) // 2)
