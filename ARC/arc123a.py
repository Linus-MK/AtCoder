a, b, c = list(map(int, input().split()))

if c-b == b-a:
    print(0)
elif c-b < b-a :
    print(2*b - a - c)
elif c-b > b-a :
    if (a+c) % 2 == 0:
        print((a+c)//2 - b)
    else:
        print((a+1+c)//2 - b + 1)
