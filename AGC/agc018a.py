import fractions

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

if n == 1:
    print("POSSIBLE" if arr[0] == k else "IMPOSSIBLE")
else:
    # 最大公約数
    gcd = arr[0]
    for num in arr[1:]:
        gcd = fractions.gcd(gcd, num)

    print("POSSIBLE" if (k % gcd == 0 and k <= max(arr)) else "IMPOSSIBLE")
