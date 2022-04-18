s = input()
if s == "".join(reversed(s)):
    print("Yes")
    exit()
else:
    num_a = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != "a":
            num_a_back = len(s) - i - 1
            break
    for i in range(len(s)):
        if s[i] != "a":
            num_a_for = i
            break
    if num_a_back > num_a_for:
        ss = "a" * (num_a_back - num_a_for) + s
        if ss == "".join(reversed(ss)):
            print("Yes")
            exit()

print("No")
