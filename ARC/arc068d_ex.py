# 解説を読むと非常にシンプルな別解があった。
# カードの山に k 種類のカードがあったとして，k が奇数なら余っているカードは偶数枚あるの
# で答えは k であり，偶数ならばどこかで必ず 1 枚しかないカードを 1 回取り除く必要があるので
# 答えは k − 1 となります．

n = int(input())
nums = list(map(int, input().split()))

k = len(set(nums))
print(k if k % 2 == 1 else k-1)
