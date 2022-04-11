temp = []
for _ in range(3):
    temp.append(input())

order = input()
ans_str = [temp[int(i) - 1] for i in order]
print("".join(ans_str))
