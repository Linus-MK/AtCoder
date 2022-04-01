a = input()
inta = int(a)

if inta % 1111 == 0:
    print("Weak")
    exit()
if a in "0123456789012":
    print("Weak")
    exit()
print("Strong")
