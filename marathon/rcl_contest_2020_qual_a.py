
ans_list = []
ans_list += [j for j in range(i+1) for i in range(8)]
ans_list += [i&7 for i in range(1000-72)]
ans_list += [j for j in range(i, 8) for i in range(8)]

for rep in range(10000):
    pass

for i in ans_list:
    print(i) 

# for i in range(8):
#     for j in range(i+1):
#         print(j)

# for i in range(1000 - 72):
#     print(i % 8)

# for i in range(8):
#     for j in range(i, 8):
#         print(j)
