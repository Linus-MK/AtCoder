n = int(input())
segment = []
for i in range(n):
    nums = list(map(int, input().split()))
    segment.append(nums)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        # 重なってない条件を書いたほうが楽。リーダブルコードにも書いてあるけど。
        if segment[i][2] < segment[j][1]:
            pass
        elif segment[j][2] < segment[i][1]:
            pass
        elif segment[i][2] == segment[j][1] and (segment[i][0] == 2 or segment[i][0] == 4 or segment[j][0] == 3 or segment[j][0] == 4):
            pass
        elif segment[j][2] == segment[i][1] and (segment[j][0] == 2 or segment[j][0] == 4 or segment[i][0] == 3 or segment[i][0] == 4):
            pass
        else:
            ans += 1
print(ans)
