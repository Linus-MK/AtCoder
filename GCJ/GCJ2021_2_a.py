# インタラクティブ interactive
# i〜100の最小値を調べる→i番目に持ってくる、をやればよい
import sys

t, n = list(map(int, input().split()))

for ti in range(t):
    for i in range(1, 99+1):
        print("M {} {}".format(i, 100))
        sys.stdout.flush()
        result = int(input())
        if result == i:
            # swapに同じ数を指定はできないのでエラーになる。何もしない
            pass
        else:
            print("S {} {}".format(i, result))
            sys.stdout.flush()
            result = int(input())
            if result != 1:
                # なんか変
                print("oops")
                exit()

    print("D")
    sys.stdout.flush()
    result = int(input())
    if result != 1:
        # なんか変
        print("oops")
        exit()

# 全てのテストケースに正解した後に
exit()

