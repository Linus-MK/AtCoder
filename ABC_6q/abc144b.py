res = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == res:
            print("Yes")
            exit()

print("No")
