n_test = int(input())
import math

for _ in range(n_test):
    n, m = list(map(int, input().split()))

    if m >= (n-1):
        minimum = 1
    else:
        minimum = n - m
    
    maximum = 0
    if m == 0:
        dec_minimum = 0
    elif m == 1:
        dec_minimum = 1
    elif 2 <= m <= 3:
        dec_minimum = 2
    else:
        temp = int(math.sqrt(m * 2)) - 1
        for t2 in range(temp, temp + 5):
            if m <= t2 * (t2+1) // 2:
                dec_minimum = t2
                break
        
    maximum = n - dec_minimum

    print(f'{minimum} {maximum}')
