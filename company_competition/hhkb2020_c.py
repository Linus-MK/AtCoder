# 次々と入れていって、途中で随時ソートする、をしたい→こういうときは優先度付きキューが便利

# 解説見たら別に優先度付きキューを使わなくても解けるらしい…… https://atcoder.jp/contests/hhkb2020/editorial/175

import heapq
n = int(input())
nums = list(map(int, input().split()))

prio_queue = []
min_now = 0
for i in range(n):
    heapq.heappush(prio_queue, nums[i])
    while len(prio_queue) and prio_queue[0] <= min_now:
        pop = heapq.heappop(prio_queue)
        if pop == min_now:
            min_now += 1

    print(min_now)

