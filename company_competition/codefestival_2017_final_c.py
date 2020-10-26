# 解法メモ
# 同じ値をとってる人が何人いるか考える。
# 0 <= Di <= 12 に注意!
# 1〜11の場合
## 3つあると、少なくとも2つは必ず一致する（鳩の巣原理）ので、その2人の時差は0になる
## 2つあると、同方向にすると時差0が確定なので、逆方向にしたほうが結果は大きくなる、逆方向で決めつけて良い
## 1つあると? これは分からない。こうなる数は高々11個なので、全探索で通る。
# 0の場合
## 1つあると、高橋くんとの時差が0になる
# 12の場合
## 2つあると、必ず一致するので、その2人の時差は0になる
## 1つあると、12で確定

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

# 0があるか
if nums[0] == 0:
    print(0)
    exit()

# 各値が何人いるか? 辞書で良さそう

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

num_one = 0
fixed = [0]  # 高橋くんの時差
for key, value in freq.items():
    if value >= 3:
        print(0)
        exit()
    if key == 12 and value >= 2:
        print(0)
        exit()
    if key < 12 and value == 1:
        num_one += 1
    if key < 12 and value == 2:
        fixed.append(key)
        fixed.append(-key)
    if key == 12 and value == 1:
        fixed.append(key)

# print(freq)


ans = 0
for idx in range(2 ** num_one):
    timegap = fixed.copy()
    digit = 0
    for key, value in freq.items():
        if key < 12 and value == 1:
            if 2**digit & idx:
                timegap.append(key)
            else:
                timegap.append(-key)
            digit += 1
    
    # 要素数の全パターンを調べなくても、ソートして隣接要素の差分を調べれば良い
    # 最大と最小の時差も考慮することに注意

    timegap.sort()
    min_dif = 24
    for i in range(len(timegap) - 1):
        min_dif = min(min_dif, timegap[i+1] - timegap[i])
    min_dif = min(min_dif, timegap[0] - timegap[-1] + 24)

    ans = max(ans, min_dif)
    # print(timegap, min_dif)

print(ans)
