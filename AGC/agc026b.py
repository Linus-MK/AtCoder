import math

t = int(input())

for i in range(t):
    a, b, c, d = list(map(int, input().split()))

    if b > d:
        # 増える本数より減る本数のほうが多いので、ジュースの本数は目減りしていつか無くなる
        print('No')
        continue
    if a < b:
        # 初日に買おうとしたらないパターン
        print('No')
        continue
    if b == d:
        # 増える本数と減る本数が同じ。一往復が可能なら永遠にループする

        if a <= c:
            # 初日に買えることは確定、その後無限ループに入る
            print('Yes')
            continue

        diff = a-c
        buy_num = (diff + b - 1) // b
        if a - buy_num * b < 0:
            print('No')
            continue
        else:
            print('Yes')
            continue
    
    if b < d:
        # 補題
        # 減少幅b と増加幅dが互いに素であれば、無限回の操作の中で取りうる最小値はc-b+1である。
        # （開店時の値の中で取りうる最小値はc+1である、のほうが分かりやすいかも?）
        # 証明：
        # (1) c-b+1を取ることがあることの証明
        # 互いに素なので、bを引いてdを足すのを繰り返すと、mod bでc+1と合同になるときが存在する。（逆元を考えれば良い）
        # このとき、購入後がc+1+b*n(n>=0) だったら、cより真に大きいので補充されない。購入だけが続く。
        # したがって、(c+1+b → 購入 →) c+1 → 購入 → c-b+1 → 補充 → c-b+1+d という動きになるときがある。
        # (2) c-b以下を取ることがないことの証明
        # 1回以上、c以上の値を取ったあとは、購入・補充（-b+dで真に増える）か購入(-b)かのどちらか。
        # 後者が発生したときは購入後の値はc+1以上でなければならない。したがって開店時の値は常にc+1以上である。
        # 購入後の値もc-b+1以上である。
        # 以上で証明完。最初からc以下の場合が曲者だが、初日に無いパターンは除外されているので、
        # 初日を乗り切れば増加してc以上の値を取るところまで行ける。すなわち上と同じ話に帰着できる。

        if math.gcd(b, d) == 1:
            if c-b+1 >= 0:
                print('Yes')
                continue
            else:
                print('No')
                continue
        else:
            # 互いに素でない場合。
            # aからgcd(b, d)ずつ引いた数列のうち、c+1以上で最小の要素が 開店時の値の中で取りうる最小値である。
            # 証明はしてないけど上とほとんど同様でしょう。
            g = math.gcd(b, d)
            diff = a - (c+1)
            subtract_width = diff // g * g
            if a - subtract_width >= b:
                print('Yes')
                continue
            else:
                print('No')
                continue                

