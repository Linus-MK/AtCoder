char = input()
for i in range(4):
    if char[-1] == "0" or char[-1] == ".":
        char = char[:-1]
    else:
        break

print(char)
