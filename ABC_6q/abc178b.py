a, b, c, d = list(map(int, input().split()))
print(max(a*c, b*c, a*d, b*d))

# ACしたあとにこれで行けることの証明：
# これ以外の積を1つ取る。つまり、x, yのどちらかは両端以外である。
# このとき、xが両端以外だとしよう。
# yが正または負の場合、yの符号に応じてxを正または負の方向に動かすと積が真に大きくなる。
# したがって、x*yは最大になりえない。
# yが0の場合、xを端点にしても積は変わらない。したがって、端点どうしの積だけ考えれば良い。
