# 直感的に分かる貪欲（下から組を作る）だと思うんだけど、これでdiff1185は数字が高すぎじゃない? 
# 貪欲で取っていくのを考えると、非ゼロの区間が連続する場合、その連続に対して下からペアを作って、最後に0か1だけ残ることがわかり、
# 単純に書ける。こんなふうに。

n = int(input())
nums = [int(input()) for _ in range(n)]

ans = 0
temp = 0
for m in nums:
    if m == 0:
        ans += temp // 2
        temp = 0
    else:
        temp += m
ans += temp // 2
print(ans)
