a = input()
b = input()

if a == b:
    print("Yes")
    exit()
for i in range(len(a) - 1):
    x = a[:i] + a[i+1] + a[i] + a[i+2:]
    # print(x)
    if x == b:
        print("Yes")
        exit()
print("No")
