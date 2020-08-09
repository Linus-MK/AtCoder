from collections import deque

k = int(input())

deq = deque()
for i in range(1, 10):
    deq.append(i)

for idx in range(k):
    ret = deq.popleft()
    # retの右に1つ付け加えてできるルンルン数を追加
    residue = ret % 10
    if residue != 0:
        deq.append(ret * 10 + residue - 1)
    
    deq.append(ret * 10 + residue)

    if residue != 9:
        deq.append(ret * 10 + residue + 1)

print(ret)
