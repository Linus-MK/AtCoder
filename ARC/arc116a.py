t = int(input())
for i_test in range(t):
    n = int(input())
    if n % 2 == 1:
        print("Odd")
    elif n % 4 != 0:
        print("Same")
    else:
        print("Even")
