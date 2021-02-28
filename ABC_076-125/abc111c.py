# 難易度の割に重実装だと思います。
# 基本的には、偶数番目、奇数番目に分けて頻度を集計し、最多のものに変えるのが最小で済む
# だがその数が一致した場合だと条件を満たさない。
# 複数の数が頻度最多の場合もある。地味に色々面倒くさい……

n = int(input())
nums = list(map(int, input().split()))

even_freq = {}
odd_freq = {}

for i in range(0, n, 2):
    elem = nums[i]
    even_freq[elem] = even_freq.get(elem, 0) + 1

for i in range(1, n, 2):
    elem = nums[i]
    odd_freq[elem] = odd_freq.get(elem, 0) + 1

odd_max = max(odd_freq.values())
odd_max_num = [k for k in odd_freq.keys() if odd_freq[k] == odd_max]

even_max = max(even_freq.values())
even_max_num = [k for k in even_freq.keys() if even_freq[k] == even_max]

# 頻度最多になる数が2つ以上あるなら、必ず異なる数による組み合わせがあるので、
if len(odd_max_num) >= 2 or len(even_max_num) >= 2:
    print(n - odd_max - even_max)
# 頻度最多になる数は1つずつである。これが異なる数なら問題ない
elif odd_max_num[0] != even_max_num[0]:
    print(n - odd_max - even_max)
else:
    # 頻度最多になる数が同じである。これに書き換えると1種類の数の数列になるので不適。
    # 偶奇のどちらかを、二番目に出現頻度が多い数に譲る必要がある。どちらのほうが変える個数が少なくなるか調べる。
    # ただしそもそも偶数側が1種類の数字だけ (tが空リスト) という場合もあり、その場合はその場合はmaxを取るとエラーになるので別扱い
    t = [k for k in odd_freq.values() if k != odd_max]
    if t:
        odd_second_max = max(t)
    else:
        odd_second_max = 0
    t = [k for k in even_freq.values() if k != even_max]
    if t:
        even_second_max = max(t)
    else:
        even_second_max = 0

    # 変えずに済む数を最大化したいので
    temp = max(odd_second_max + even_max, odd_max + even_second_max)
    print(n - temp)
