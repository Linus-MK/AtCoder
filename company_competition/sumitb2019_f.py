# 相対速度に注目する。
# 最初の1サイクル終わって出会わないなら絶対出会わない。
# あと余りが0の場合だけは特別扱いになる。

t1, t2 = list(map(int, input().split()))
a1, a2 = list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))

first = t1 * (b1 - a1)
second = t2 * (b2 - a2)

if first > 0 and first + second > 0:
    print(0)
elif first < 0 and first + second < 0:
    print(0)
elif first + second == 0:
    print('infinity')
else:
    temp = abs(first) // abs(first + second)
    mod = abs(first) % abs(first + second)

    if mod == 0:
        ans = temp * 2
    else:
        ans = temp * 2 + 1
    
    print(ans)

