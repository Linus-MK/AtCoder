# 写像はどこか（操作N回以内）でループに入るので、それ以降は周期と剰余を使って求める。
# これはO(n^2)なのでTLE

n, k = list(map(int, input().split()))
perm = list(map(int, input().split()))
perm = [i-1 for i in perm]
initial_nums = list(map(int, input().split()))

if k == 0:
    ans = map(str, initial_nums)
    print(" ".join(ans))
    exit()

ans = [-1] * n
for i in range(n):
    pos_dict = dict()
    pos_dict_inverce = dict()

    perm_count = 0
    pos_dict[i] = 0
    pos_dict_inverce[0] = i
    pos = i

    for c in range(1, n+1):
        pos = perm[pos]

        if pos_dict.get(pos) is not None:
            # 訪問済み。ループができた
            loop_period = c - pos_dict[pos]
            # ループの中にしなければいけないので、 c % loop_period ではない
            temp = (k - c) // loop_period 
            back = (temp + 1) * loop_period
            index = k - back
            ans[i] = initial_nums[pos_dict_inverce[index]]
            break

        else:
            pos_dict[pos] = c
            pos_dict_inverce[c] = pos

            if c == k:
                ans[i] = initial_nums[pos]
                break

# print(ans)
ans = map(str, ans)
print(" ".join(ans))
