# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1284

# インタラクティブ問題だ! 1年ぶりだ!

# テストセット1 10C3 = 120 < 300なので、3つの組み合わせを全通り質問して、あとは適合するのをうまく探せば良さそう
# （具体的な方法分からんけど）

# テストセット2
# 両端の数ってどうすれば分かる?
# 適当に3つ聞いて、中央値のやつは両端になりえない。だから、50個から適当に3つ聞いて、中央値を
# AとCが両端だとする。適当にBを持ってくるとA-B-Cだ。
# A,B,他 を全部聞いて、A-B間とB-C間のどっちにあるか判定する。
# その後、それぞれに対してまた同じことをやる（分割統治法）
# ……これ300回でできるか怪しいと思う。2^6=64で、Bが真ん中に来ない可能性とか考えると、厳しそう。

# ABCがこの順だとする。
# Dがどこに入るか知りたい。4通りある。A,B,Dを聞いて、Bが真ん中だとBより右なのでB,C,Dを聞けば確定する。
# 一般に、n個の列に対して新しい要素がどこに入るか知りたい場合、候補はn+1個あり、
# 50*50/2/2=625 > 300だダメだ。
# ここを2分探索か。すると高々50*log(50)/2 = 50*6/2=150でいけそう。
# いやこれ170のhidden caseも通るのでは?
# →通りませんでした。なんでだろう

import sys

n_test, n, q = list(map(int, input().split()))

# if q == 170 * n_test:
#     exit()
for i_test in range(n_test):

    print("1 2 3", flush=True)
    ret = int(input())
    if ret == 1:
        current_list = [2, 1, 3]
    elif ret == 2:
        current_list = [1, 2, 3]
    elif ret == 3:
        current_list = [1, 3, 2]
    
    for elem in range(4, n+1):
        # elemをどこに入れるか2分探索しよう

        print(f"{current_list[0]} {current_list[-1]} {elem}", flush=True)
        ret = int(input())
        if ret == current_list[0]:
            current_list = [elem] + current_list
            continue
        elif ret == current_list[-1]:
            current_list = current_list + [elem]
            continue
        
        index_upper = len(current_list) - 1
        index_lower = 0


        # めぐる式二分探索
        while abs(index_upper - index_lower) > 1:
            mid = (index_upper + index_lower) // 2
            print(f"{current_list[index_lower]} {current_list[mid]} {elem}", flush=True)
            ret = int(input())
            if ret == elem:
                index_upper = mid
            else:
                index_lower = mid

        current_list = current_list[:index_upper] + [elem] + current_list[index_upper:]
        

    str_array = list(map(str, current_list))
    print(" ".join(str_array))
    ret = int(input())

    if ret != 1:
        # 不正解だ
        exit()

