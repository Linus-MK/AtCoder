# ある集合を入れるか入れないかだよね
# 2-(条件を満たす部分集合の数) - 1
# 適当な数aからa f(a) f(f(a))……をやって、aに戻ってきたらOK、一度訪問したところに来たら不可

n = int(input())
nums = list(map(int, input().split()))
nums = [a-1 for a in nums] # 1減らします

num_of_subset = 0
visited = [False] * n
for a in range(n):
    if visited[a]:
        continue
    current_chain = set()
    current_chain.add(a)

    cur = a
    while True:
        cur = nums[cur]
        if visited[cur]:
            if cur in current_chain:
                num_of_subset += 1
                break
            else:
                break

        else:
            visited[cur] = True
            current_chain.add(cur)

mod = 998244353
ans = pow(2, num_of_subset, mod) - 1
print(ans)
