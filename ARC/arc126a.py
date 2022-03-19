n_test = int(input())

for _ in range(n_test):
    two, three, four = map(int(), input().split())
    # 2-2-2-2-2
    # 2-2-3-3
    # 3-3-4
    # 2-4-4
    # 2-2-2-4

    ans = 0
    # まず3-3-4
    temp = min(three//2, four)
    three -= temp * 2
    four -= temp
    ans += temp

    # 3-3-2-2
    temp = min(three//2, two//2)
    three -= temp * 2
    two -= temp * 2
    ans += temp

    # 2-4-4
    temp = min(two, four//2)
    two -= temp
    four -= temp * 2
    ans += temp

    # 2-2-2-4
    temp = min(two//3, four)
    two -= temp * 3
    four -= temp
    ans += temp

    temp = two//5
    two -= temp * 5
    ans += temp


    print(ans)

