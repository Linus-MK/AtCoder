n, a, b, c = list(map(int, input().split()))
command = [input() for i in range(n)]

summ = a + b + c
if summ == 0:
    print('No')
    exit()

if summ >= 3:
    if command[0] == 'AB' and summ == c or command[0] == 'BC' and summ == a or command[0] == 'AC' and summ == b:
        print('No')
    else:
        print('Yes')
        for com in command:
            if com == 'AB':
                if a == 0:
                    print('A')
                    a += 1
                    b -= 1
                elif b == 0:
                    print('B')
                    a -= 1
                    b += 1
                elif a == 1:
                    print('A')
                    a += 1
                    b -= 1
                else:
                    print('B')
                    a -= 1
                    b += 1
            if com == 'BC':
                if b == 0:
                    print('B')
                    b += 1
                    c -= 1
                elif c == 0:
                    print('C')
                    b -= 1
                    c += 1
                elif b == 1:
                    print('B')
                    b += 1
                    c -= 1
                else:
                    print('C')
                    b -= 1
                    c += 1
            if com == 'AC':
                if c == 0:
                    print('C')
                    c += 1
                    a -= 1
                elif a == 0:
                    print('A')
                    c -= 1
                    a += 1
                elif c == 1:
                    print('C')
                    c += 1
                    a -= 1
                else:
                    print('A')
                    c -= 1
                    a += 1


elif summ == 2:
    choice = [''] * n
    for i, com in enumerate(command):

        if com == 'AB':
            if c == 2:
                print('No')
                exit()
            if a == 0:
                choice[i] = 'A'
                a += 1
                b -= 1
            elif b == 0:
                choice[i] = 'B'
                a -= 1
                b += 1
            else:
                if i < n-1 and command[i+1] == 'BC':
                    choice[i] = 'B'
                    a -= 1
                    b += 1
                else:
                    choice[i] = 'A'
                    a += 1
                    b -= 1
        if com == 'BC':
            if a == 2:
                print('No')
                exit()
            if b == 0:
                choice[i] = 'B'
                b += 1
                c -= 1
            elif c == 0:
                choice[i] = 'C'
                b -= 1
                c += 1
            else:
                if i < n-1 and command[i+1] == 'AC':
                    choice[i] = 'C'
                    b -= 1
                    c += 1
                else:
                    choice[i] = 'B'
                    b += 1
                    c -= 1


        if com == 'AC':
            if b == 2:
                print('No')
                exit()
            if c == 0:
                choice[i] = 'C'
                c += 1
                a -= 1
            elif a == 0:
                choice[i] = 'A'
                c -= 1
                a += 1
            else:
                if i < n-1 and command[i+1] == 'AB':
                    choice[i] = 'A'
                    c -= 1
                    a += 1
                else:
                    choice[i] = 'C'
                    c += 1
                    a -= 1
    
    print('Yes')
    for ch in choice:
        print(ch)



elif summ == 1:
    # １つずつシミュレーション

    choice = [''] * n
    for i, com in enumerate(command):
        if com == 'AB':
            if c == 1:
                print('No')
                exit()
            if a == 0:
                choice[i] = 'A'
                a += 1
                b -= 1
            elif b == 0:
                choice[i] = 'B'
                a -= 1
                b += 1
        if com == 'BC':
            if a == 1:
                print('No')
                exit()
            if b == 0:
                choice[i] = 'B'
                b += 1
                c -= 1
            elif c == 0:
                choice[i] = 'C'
                b -= 1
                c += 1


        if com == 'AC':
            if b == 1:
                print('No')
                exit()
            if c == 0:
                choice[i] = 'C'
                c += 1
                a -= 1
            elif a == 0:
                choice[i] = 'A'
                c -= 1
                a += 1
    
    print('Yes')
    for ch in choice:
        print(ch)

