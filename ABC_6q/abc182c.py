n = input()
int_n = int(n)

if len(n) == 1:
    print(0 if int_n % 3 == 0 else -1)
else:
    if int_n % 3 == 0:
        print(0)
    elif int_n % 3 == 1:
        if '1' in n or '4' in n or '7' in n:
            print(1)
        else:
            if len(n) > 2:
                print(2)
            else:
                print(-1)
    elif int_n % 3 == 2:
        if '2' in n or '5' in n or '8' in n:
            print(1)
        else:
            if len(n) > 2:
                print(2)
            else:
                print(-1)
