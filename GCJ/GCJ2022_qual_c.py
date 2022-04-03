# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471

N = int(input())
for i_test in range(N):

    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    current = 1
    for i in range(n):
        if nums[i] >= current:
            current += 1
        else:
            continue
    print(f"Case #{i_test+1}: {current - 1}")
