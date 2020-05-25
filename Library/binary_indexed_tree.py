n = int(input())

# 蟻本のp.159

# Binary Indexed Tree = BIT
# 1-indexで管理するのが良いらしい。
# できることは、
# * ある要素にある値を足す
# * 最初から指定位置までの和を求める
# いずれも計算量はO(log(n))

bit = [0] * (n+1)


def calc_sum(i):
    s = 0
    while (i > 0):
        s += bit[i]
        i -= i & -i
    return s


def add(idx, num):
    while (idx <= n):
        bit[idx] += num
        idx += idx & -idx


def print_sum(i):
    print("{}番目までの和は{}です。".format(i, calc_sum(i)))


print(bit)
add(2, 4)
print(bit)
add(1, 5)
print(bit)
print_sum(1)
print_sum(2)
add(6, 8)
print(bit)
print_sum(1)
print_sum(2)
print_sum(3)
print_sum(5)
print_sum(6)
print_sum(7)
