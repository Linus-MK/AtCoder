import sys

t, a, b = list(map(int, input().split()))
length = 10**9

if a != b:
    exit()
    # テストセット3

for ti in range(t):
    # 左右中央から100左のところを最上から順に当てる
    # 内部になりえるのは1〜101なので、101を含めて必ずif文の中に入れてbreakさせる
    for i in range(100 + 2):
        print("{} {}".format(-100, length - i))
        sys.stdout.flush()
        result = input()
        if result == "HIT":
            break
    y_coord = length - (i-1) - a
    
    # 上下中央から100下のところを最右から順に当てる
    for i in range(100 + 2):
        print("{} {}".format(length - i, -100))
        sys.stdout.flush()
        result = input()
        if result == "HIT":
            break
    x_coord = length - (i-1) - a

    print("{} {}".format(x_coord, y_coord))
    sys.stdout.flush()
    result = input()
    if result != "CENTER":
        # なんか変
        print("oops")
        exit()

# 全てのテストケースに正解した後に
exit()
