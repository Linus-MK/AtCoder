import heapq

# 優先度付きキューは「最も値が小さいもの」を出すことに注意

prio = []
n_query = int(input())
plus = 0

for i in range(n_query):
    nums =list(map(int, input().split()))

    if nums[0] == 1:
        num = nums[1]
        heapq.heappush(prio, num-plus)
    elif nums[0] == 2:
        plus += nums[1]
    elif nums[0] == 3:
        temp = heapq.heappop(prio)
        print(temp+plus)
