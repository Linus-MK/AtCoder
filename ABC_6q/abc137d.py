n, deadline =  list(map(int, input().split() ))

# 要素を入れる、popで最大のものを取り出す　優先度付きキューじゃん
# pythonでは最小のものが出てくるので注意

tasks = [list(map(int, input().split() )) for _ in range(n)]

from operator import itemgetter, attrgetter
tasks.sort(key = itemgetter(0))

idx_t = 0
ans = 0
import heapq

prio_queue = []
for today in range(deadline, -1, -1):

	span = deadline - today
	while(idx_t < n and tasks[idx_t][0] == span):
		heapq.heappush(prio_queue, -1 * tasks[idx_t][1])
		idx_t += 1
	
	if len(prio_queue) > 0:
		a = heapq.heappop(prio_queue)
		ans += -a

print(ans)

