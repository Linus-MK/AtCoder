a, b = input().split()
a = int(a)

b100 = int(b[0])*100 + int(b[2])*10 + int(b[3])
print(a * b100 // 100)
