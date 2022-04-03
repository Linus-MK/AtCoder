# hhttps://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

# 言われたことをそのまま再現すればよい。

def cells(n):
    return "|." * n + "|"

def borders(n):
    return "+-" * n + "+"

N = int(input())
for i_test in range(N):

    r, c = list(map(int, input().split()))

    print("Case #{0}:".format(i_test+1))
    for i in range(r):
        if i == 0:
            print('..' + borders(c-1))
            print('..' + cells(c-1))
        else:
            print(borders(c))
            print(cells(c))
    print(borders(c))
