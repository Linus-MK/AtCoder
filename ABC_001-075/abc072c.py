n = int(input())
nums = list(map(int, input().split()))

freq = [0] * 10**5
for num in nums:
    freq[num] += 1

ans = 0
for a in range(1, 10**5-1):
    ans = max(ans, freq[a-1] + freq[a] + freq[a+1])
    # 差分だけ加減算することで高速化はできるけど、今回別にそれをやる必要はない
print(ans)
