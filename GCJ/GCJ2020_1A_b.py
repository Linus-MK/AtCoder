# URL

N = int(input())
for ix in range(N):
    num = int(input())

    print("Case #{0}:".format(ix+1))

    summ = 0
    print("{} {}".format(1, 1))
    summ += 1
    if summ == num:  # num=1
        continue

    for i in range(2, 1000):
        print("{} {}".format(i, 2))
        summ += (i-1)
        if summ + i > num:
            break

    if summ == num:  # num=三角数+1
        continue

    pos = i
    for i in reversed(range(2, pos+1)):
        print("{} {}".format(i, 1))
        summ += 1
        if summ == num:
            break

    # assert(summ == num)

