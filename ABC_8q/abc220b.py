k = int(input())
a, b = input().split()

a_int = 0
for i in range(len(a)):
    a_int += int(a[i]) * k ** (len(a) - i - 1)
b_int = 0
for i in range(len(b)):
    b_int += int(b[i]) * k ** (len(b) - i - 1)
print(a_int*b_int)
